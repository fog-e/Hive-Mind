import os
from dotenv import load_dotenv

# Load API key and other environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# TEMP: check that the key loads
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing from your .env file.")

# === Placeholder vector search ===
def mock_vector_search(query: str):
    print(f"[LOG] Searching FAQ for: {query}")
    # This would call your vector DB search tool
    return "Bees typically swarm in late spring. Preventative measures include splitting and providing ample space."

# === Main loop ===
if __name__ == "__main__":
    print("🤖 Apis Munificent activated.")
    user_input = input("Ask me a beekeeping question: ")
    response = mock_vector_search(user_input)
    print(f"\n🧠 Answer: {response}")
