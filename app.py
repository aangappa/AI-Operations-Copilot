from logs import logging_config
from services.knowledge_cache import (
    load_knowledge_cache,
    knowledge_cache
)
from orchestrator.orchestrator import process_incident
from dotenv import load_dotenv
from services.vector_index import build_index
import logging

load_dotenv()



print("AI Operations Copilot Started")

logging.info("Loading Incident")
knowledge = load_knowledge_cache()
build_index(knowledge)
response = process_incident()

logging.info("Gemini response received")

print(response)