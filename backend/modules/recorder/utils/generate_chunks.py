from langchain.text_splitter import CharacterTextSplitter

def generate_chunks(text:str):
    n = 1000
    chunks = [text[i:i+n] for i in range(0, len(text), n)]
    return chunks