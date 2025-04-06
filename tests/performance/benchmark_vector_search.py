import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def benchmark_vector_search():
    # Simulate a large set of vectors
    database_vectors = np.random.rand(10000, 300)
    query_vector = np.random.rand(1, 300)

    start = time.time()
    similarities = cosine_similarity(query_vector, database_vectors)
    top_k_indices = similarities[0].argsort()[-5:][::-1]
    duration = time.time() - start

    print(f"Top-5 indices: {top_k_indices}")
    print(f"Search time: {duration:.4f} seconds")

if __name__ == "__main__":
    benchmark_vector_search()
