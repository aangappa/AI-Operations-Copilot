import os


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

            if word in content.lower():
                score += 1

        if score > highest_score:
            highest_score = score
            best_match = content

    if best_match:
        return best_match

    return "No matching knowledge found."