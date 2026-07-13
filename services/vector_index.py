import faiss
import numpy as np

index = None
documents = []


def build_index(knowledge_cache):

    global index
    global documents

    documents = knowledge_cache

    dimension = len(
        knowledge_cache[0]["embedding"]
    )

    index = faiss.IndexFlatL2(dimension)

    vectors = np.array(
        [doc["embedding"] for doc in knowledge_cache],
        dtype="float32"
    )

    index.add(vectors)

    print(
        f"FAISS Index built with {index.ntotal} vectors."
    )


def search(query_embedding, top_k=3):

    query = np.array(
        [query_embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        query,
        top_k
    )

    results = []

    for distance, idx in zip(
        distances[0],
        indices[0]
    ):

        results.append({

            "filename": documents[idx]["filename"],

            "content": documents[idx]["content"],

            "distance": float(distance)

        })

    return results