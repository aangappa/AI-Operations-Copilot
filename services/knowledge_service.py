import os

from services.embedding_service import (
    create_embedding,
    similarity
)


def get_knowledge(incident):

    title = incident.shortdescription

    incident_embedding = create_embedding(title)

    results = []

    knowledge_folder = "knowledge"

    for filename in os.listdir(knowledge_folder):

        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(
            knowledge_folder,
            filename
        )

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        document_embedding = create_embedding(content)

        score = similarity(
            incident_embedding,
            document_embedding
        )

        print(f"{filename} -> {score:.3f}")

        results.append({
            "filename": filename,
            "score": score,
            "content": content
        })

    if not results:
        return "No knowledge found."

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    top_results = results[:3]

    knowledge = ""

    for item in top_results:

        knowledge += f"""
==================================================

Knowledge Article:
{item['filename']}

Similarity Score:
{item['score']:.3f}

{item['content']}

"""

    return knowledge