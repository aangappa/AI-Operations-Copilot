from logs import logging_config
from orchestrator.orchestrator import process_incident

import logging

print("AI Operations Copilot Started")

logging.info("Loading Incident")

response = process_incident()

logging.info("Gemini response received")

print(response)