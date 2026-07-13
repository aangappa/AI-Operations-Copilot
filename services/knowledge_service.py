from services.embedding_service import create_embedding
from services.vector_index import search


def get_knowledge(incident):

    incident_embedding = create_embedding(
        incident.shortdescription
    )

    results = search(
        incident_embedding,
        top_k=3
    )

    knowledge = ""

    for item in results:

        print(
            f"{item['filename']} -> Distance {item['distance']:.4f}"
        )

        knowledge += f"""
==================================================

Knowledge Article:
{item['filename']}

Distance:
{item['distance']:.4f}

{item['content']}

"""

    return knowledge