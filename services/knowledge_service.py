import os
from services.knowledge_cache import knowledge_cache

from services.embedding_service import (
    create_embedding,
    similarity
)


def get_knowledge(incident):

    title = incident.shortdescription

    incident_embedding = create_embedding(title)

    results = []

    for document in knowledge_cache:

        score = similarity(
            incident_embedding,
            document["embedding"]
        )

        print(f'{document["filename"]} -> {score:.3f}')

        results.append({

            "filename": document["filename"],

            "score": score,

            "content": document["content"]

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