# Hive-Mind   
**An autonomous agent for answering FAQ questions about beekeeping.**

## Agent: Apis Munificent
Apis Munificent is a role-based AI agent designed to answer common questions using the official FAQ from a regional beekeeping organization. The agent runs within the Hive-Mind system—an intelligent network of seasonal, task-focused agents.

## Project Goals
- Answer beekeeping questions using vector search from the FAQ
- Maintain accuracy and friendly tone
- Support future multi-agent expansions (newsletters, event reminders, etc.)

## Tools & Tech
- Python
- Vector store (Chroma or FAISS)
- Custom prompt templates
- Optional scraping tool for FAQ refresh

## Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Optional: create your .env for any API keys or configs
cp .env.example .env
