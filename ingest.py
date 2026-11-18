
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCUMENTS_DIR = Path("documents")


def load_and_split_pdfs(pdf_paths=None):

    if pdf_paths is None:
        pdf_files = list(DOCUMENTS_DIR.glob("*.pdf"))
    else:
        pdf_files = [Path(path) for path in pdf_paths]

    if not pdf_files:
        print("No PDF files found!")
        return []

    all_chunks = []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    for pdf_file in pdf_files:

        print(f"\nReading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))
        pages = loader.load()

        for page in pages:
            page.metadata["source"] = pdf_file.name
            page.metadata["page_number"] = page.metadata.get("page", 0) + 1

        chunks = text_splitter.split_documents(pages)

        all_chunks.extend(chunks)

        print(f"Pages extracted: {len(pages)}")
        print(f"Chunks created: {len(chunks)}")

    print("\nPDF processing completed!")
    print(f"Total chunks: {len(all_chunks)}")

    return all_chunks


if __name__ == "__main__":
    documents = load_and_split_pdfs()
