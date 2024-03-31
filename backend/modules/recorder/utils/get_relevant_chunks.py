from backend.modules.recorder.utils.get_vector_store import get_vector_store


def get_relevant_chunks(question: str, number_of_chunks: int = 5):
    store = get_vector_store().as_retriever()
    relevent = store.get_relevant_documents(question)
    
    chunks_contents = [
        document.page_content for document in relevent[:number_of_chunks]
    ]

    return "\n".join(chunks_contents)
