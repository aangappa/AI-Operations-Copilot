from services.incident_loader import load_incident
from services.knowledge_service import get_knowledge
from prompt_builder import build_prompt
from services.ai_service import ask_ai


def process_incident():

    incident = load_incident()

    if incident.priority == "P1":
        knowledge = get_knowledge(incident)
    else:
        knowledge = "Knowledge retrieval skipped."

    prompt = build_prompt(
        incident,
        knowledge
    )

    response = ask_ai(prompt)

    return response