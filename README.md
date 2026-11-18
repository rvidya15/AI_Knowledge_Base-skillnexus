# 📚 AI-Powered Knowledge Base

An AI-powered document question-answering system built using Retrieval-Augmented Generation (RAG), LangChain, ChromaDB, Hugging Face embeddings, Gemini API, and Streamlit.

Upload research papers in PDF format and ask questions about their contents. The application retrieves relevant document sections and generates context-grounded answers with source information.

## 🚀 Features

- **PDF Processing:** Extract text from PDF research papers.
- **Text Chunking:** Split large documents into smaller, searchable sections.
- **Semantic Search:** Retrieve relevant content using vector embeddings.
- **Vector Database:** Store and search document embeddings using ChromaDB.
- **AI-Powered Answers:** Generate responses using Google's Gemini API.
- **Source References:** Display source document names and page information.
- **Chat Interface:** Interact with uploaded documents through Streamlit.
- **Multiple PDF Support:** Upload and process multiple PDF documents.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG pipeline and document processing |
| ChromaDB | Vector database |
| Hugging Face | Text embedding model |
| all-MiniLM-L6-v2 | Sentence embeddings |
| Google Gemini API | AI response generation |
| Streamlit | Web application interface |
| PyPDF | PDF text extraction |

## 🏗️ System Architecture

1. User uploads PDF documents.
2. PyPDF extracts text from the documents.
3. LangChain splits extracted text into smaller chunks.
4. Hugging Face converts chunks into vector embeddings.
5. ChromaDB stores the embeddings.
6. User submits a question.
7. ChromaDB retrieves the most relevant chunks.
8. Gemini generates an answer using the retrieved context.
9. The application displays the answer and source references.

## 📂 Project Structure

```text
AI_Knowledge_Base/
│
├── documents/
├── chroma_db/
├── app.py
├── ingest.py
├── rag.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

Note: `.env`, `chroma_db/`, `.venv/`, and uploaded PDF files are excluded from GitHub.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_Knowledge_Base
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

Never share your API key publicly.

### 6. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## 💬 How to Use

1. Launch the Streamlit application.
2. Upload one or more PDF research papers.
3. Process the uploaded documents.
4. Enter a question about the documents.
5. Receive an AI-generated answer.
6. Expand the source section to view supporting document references.

## 🧠 RAG Workflow

The project uses Retrieval-Augmented Generation (RAG) to improve the relevance of AI-generated answers.

Instead of answering questions using only the language model's general knowledge, the application retrieves relevant document content and supplies it as context.

This helps produce answers grounded in the uploaded documents.

## 🔮 Future Improvements

- Support additional document formats such as DOCX and TXT.
- Add duplicate-document detection.
- Improve source citation formatting.
- Add document management and deletion.
- Add conversation export functionality.
- Deploy the application online.
- Improve the user interface and user experience.

## 👩‍💻 Author

**Vidya**

AI/ML Engineering Student

Project: AI-Powered Knowledge Base

## 📄 License

This project is intended for educational and portfolio purposes.