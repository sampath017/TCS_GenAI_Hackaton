from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import settings as s


def get_db(embedding_model):
    db = Chroma(
        persist_directory=(s.data_root_path/"chroma_db").as_posix(),
        embedding_function=embedding_model
    )

    # Get all stored document metadata
    docs_data = db.get(include=["metadatas"])
    embedded_files = [meta.get(
        "source") for meta in docs_data["metadatas"] if meta.get("source") is not None]

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=100)
    for csv_file in (s.data_root_path/"csv").glob("*.csv"):
        if not csv_file.name in embedded_files:
            # Load PDF (with images if needed)
            loader = CSVLoader(file_path=csv_file, encoding="utf-8")
            all_docs = loader.load()

            # Split the docs
            docs_chunks = text_splitter.split_documents(all_docs)

            # Add to DB and persist
            db.add_documents(docs_chunks)

            print(f"File processed and indexed: {csv_file.name}")
        else:
            print(f"File already embedded and indexed: {csv_file.name}")
            break  # TEMP

    return db
