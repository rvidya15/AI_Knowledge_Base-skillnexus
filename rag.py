
from pathlib import Path
from dotenv import load_dotenv
import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

DB_PATH = Path(__file__).resolve().parent / "chroma_db"

# Load the embedding model
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# Connect to the existing ChromaDB
def get_vector_database():
    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=str(DB_PATH),
        embedding_function=embeddings,
        collection_name="research_papers"
    )

    return db

def add_documents_to_database(documents):

    if not documents:
        return 0

    db = get_vector_database()

    db.add_documents(documents)

    return len(documents)

# Ask a question using RAG
def ask_question(question):

    # Step 1: Retrieve relevant chunks
    db = get_vector_database()

    retriever = db.as_retriever(
        search_kwargs={"k": 4}
    )

    documents = retriever.invoke(question)

    if not documents:
        return "No relevant information found.", []

    # Step 2: Prepare context
    context = "\n\n".join(
        [
            f"Source: {doc.metadata.get('source', 'Unknown')}, "
            f"Page: {doc.metadata.get('page', 'Unknown')}\n"
            f"Content: {doc.page_content}"
            for doc in documents
        ]
    )

    # Step 3: Connect to Gemini
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=0
    )

    # Step 4: Create prompt
    prompt = ChatPromptTemplate.from_template("""
    You are an AI research assistant.

    Answer the question using ONLY the provided context.

    If the answer is not available in the context,
    clearly say that the document does not contain
    enough information.

    Context:
    {context}

    Question:
    {question}

    Provide a clear and simple answer.
    """)


    # Step 5: Generate answer
    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    # Extract readable answer
    answer = response.content

    if isinstance(answer, list):
        answer = "\n".join(
            item["text"]
            for item in answer
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    # Step 6: Collect sources
    sources = [
        {
            "file": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", "Unknown")
        }
        for doc in documents
    ]

    return answer, sources
