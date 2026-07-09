import os

STOP_WORDS = {
    "the",
    "is",
    "are",
    "to",
    "a",
    "an",
    "of",
    "for",
    "in",
    "on",
    "and",
    "users"
}

def get_knowledge(incident):

    title = incident.shortdescription.lower()

    knowledge_folder = "knowledge"

    best_match = None
    highest_score = 0

    for filename in os.listdir(knowledge_folder):

        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(knowledge_folder, filename)

        with open(filepath, "r", encoding="utf-8") as file:

            content = file.read()

        score = 0

        for word in title.split():

            if word in STOP_WORDS:
                continue

            if word in content.lower():
                score += 1

        if score > highest_score:
            highest_score = score
            best_match = {
                "filename": filename,
                "content": content
            }

    if best_match:
        return f"""
            Knowledge Article:
            {best_match["filename"]}

            {best_match["content"]}
        """

    return "No matching knowledge found."