from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded.")


def create_embedding(text):

    embedding = model.encode(text)

    return embedding

def similarity(vector1, vector2):

    from sklearn.metrics.pairwise import cosine_similarity

    return cosine_similarity(
        [vector1],
        [vector2]
    )[0][0]