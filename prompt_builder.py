def build_prompt(incident, knowledge):

    return f"""
You are an experienced IT Operations Engineer.

Analyze the following incident.

Incident Number: {incident.number}
Application: {incident.application}
Priority: {incident.priority}
Description:
{incident.shortdescription}

Knowledge:
{knowledge}
You have access to enterprise tools.

Use the tools only if they help your investigation.

Produce a report with:

1. Summary
2. Possible Root Cause
3. Evidence
4. Recommended Resolution
5. Next Investigation Steps
"""