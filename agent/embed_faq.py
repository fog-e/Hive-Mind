import os
import json
import chromadb
import openai
from dotenv import load_dotenv
from chromadb.config import Settings

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load FAQ entries from JSON file
with open("faq_entries.json", "r") as f:
    faq_data = json.load(f)["faq"]

# Initialize Chroma in-memory (no persistence)
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    anonymized_telemetry=False,
    persist_directory="/tmp/chroma"  # non-SQLite path
))

# Create the collection
collection = client.get_or_create_collection(name="faq")

# Extract data
documents = [entry["answer"] for entry in faq_data]
metadatas = [{"question": entry["question"], "id": entry["id"]} for entry in faq_data]
ids = [f"faq-{entry['id']}" for entry in faq_data]

# Store in Chroma
collection.add(documents=documents, metadatas=metadatas, ids=ids)

print(f"✅ Embedded {len(documents)} FAQ entries into Chroma (in-memory).")
