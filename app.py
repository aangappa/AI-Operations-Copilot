from logs import logging_config
from services.knowledge_cache import load_knowledge_cache
from orchestrator.orchestrator import process_incident
from dotenv import load_dotenv
import logging

load_dotenv()



print("AI Operations Copilot Started")

logging.info("Loading Incident")
load_knowledge_cache()
response = process_incident()

logging.info("Gemini response received")

print(response)