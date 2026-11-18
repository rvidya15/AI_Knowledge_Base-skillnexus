
import streamlit as st
from rag import ask_question, add_documents_to_database
from ingest import load_and_split_pdfs
from pathlib import Path

st.set_page_config(
    page_title="AI Knowledge Base",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Knowledge Base")
st.write("Ask questions about your uploaded research papers.")

# PDF Upload Section
st.subheader("📄 Upload Research Papers")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Process PDFs"):

    if uploaded_files:

        documents_dir = Path("documents")
        documents_dir.mkdir(exist_ok=True)

        saved_paths = []

        for uploaded_file in uploaded_files:

            file_path = documents_dir / uploaded_file.name
            file_path.write_bytes(uploaded_file.getbuffer())

            saved_paths.append(file_path)

        with st.spinner("Processing your PDFs..."):

            chunks = load_and_split_pdfs(saved_paths)

            count = add_documents_to_database(chunks)

        st.success(
            f"Successfully processed {len(uploaded_files)} PDFs "
            f"and added {count} text chunks!"
        )

    else:
        st.warning("Please upload at least one PDF.")


# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("View Sources"):
                for source in message["sources"]:
                    st.write(source)

# Chat input
question = st.chat_input("Ask something about your PDF...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching your documents..."):
            try:
                answer, sources = ask_question(question)

                st.write(answer)

                with st.expander("View Sources"):
                    for source in sources:
                        st.write(source)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except Exception as e:
                st.error(f"Something went wrong: {e}")

