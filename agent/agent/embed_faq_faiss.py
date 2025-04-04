import os
import json
import openai
import faiss
import numpy as np
from dotenv import load_dotenv

# === Load environment ===
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Load FAQ data ===
with open("faq_entries.json", "r") as f:
    faq_data = json.load(f)["faq"]

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]
ids = [str(item["id"]) for item in faq_data]

# === Embed with OpenAI ===
def get_embeddings(texts, model="text-embedding-ada-002"):
    response = openai.Embedding.create(input=texts, model=model)
    return [np.array(e["embedding"], dtype=np.float32) for e in response["data"]]

embeddings = get_embeddings(answers)

# === Store in FAISS ===
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.stack(embeddings))

# === Save the index + metadata for later
faiss.write_index(index, "data/vectorstore/faq.index")
with open("data/vectorstore/faq_meta.json", "w") as f:
    json.dump({"questions": questions, "answers": answers, "ids": ids}, f)

print(f"✅ Embedded {len(answers)} FAQs and saved to FAISS index.")
