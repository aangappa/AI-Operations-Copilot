from services.ai_service import ask_ai


def choose_tools_with_ai(incident):

    prompt = f"""
You are an IT Operations AI Agent.

Available tools:

- knowledge
- cpu
- changes

Incident:

Application: {incident.application}
Priority: {incident.priority}
Description: {incident.shortdescription}

Return ONLY the tool names separated by commas.

Example:

knowledge,cpu,changes

Do not explain your answer.
"""

    response = ask_ai(prompt)

    return response