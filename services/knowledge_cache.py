import os
import pickle   
from services.embedding_service import create_embedding

knowledge_cache = []
CACHE_FILE = "cache/knowledge_embeddings.pkl"

def load_knowledge_cache():

    global knowledge_cache

    if os.path.exists(CACHE_FILE):

        print("Loading embeddings from cache...")

        with open(CACHE_FILE, "rb") as file:

            knowledge_cache = pickle.load(file)
            return knowledge_cache

        print(
            f"Loaded {len(knowledge_cache)} articles from cache."
        )

        return

    knowledge_cache = []

    knowledge_folder = "knowledge"

    print("Generating embeddings...")

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

        embedding = create_embedding(content)

        knowledge_cache.append({

            "filename": filename,

            "content": content,

            "embedding": embedding

        })

    with open(CACHE_FILE, "wb") as file:

        pickle.dump(
            knowledge_cache,
            file
        )

    print(
        f"Generated and cached {len(knowledge_cache)} articles."
    )
    return knowledge_cache