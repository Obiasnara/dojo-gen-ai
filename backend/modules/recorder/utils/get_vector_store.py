# get_vector_store.py
 
import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import SupabaseVectorStore
from supabase.client import create_client

api_key = os.environ["OPENAI_API_KEY"]
supabase_url = os.environ["SUPABASE_URL"]
# supabase_key = os.environ["SUPABASE_KEY"]
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl2Y2RtcnZmdHNlaXdydXJwZXVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyMTYyODYsImV4cCI6MjAyMjc5MjI4Nn0.1kfnibNipDolrApg8HhOq4La34XKHmUzgQ3xVqY58zY"

def get_vector_store() -> SupabaseVectorStore:
    embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)

    supabase_client = create_client(supabase_url, supabase_key)

    vector_store = SupabaseVectorStore(
        client=supabase_client,
        embedding=embeddings_model,
        table_name="vectors",
        query_name="match_vectors",
    )

    return vector_store