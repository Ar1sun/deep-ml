import numpy as np

def cosine_similarity(v1, v2):
    v1 = np.asarray(v1)
    v2 = np.asarray(v2)

    if v1.shape != v2.shape:
        raise ValueError("Vectors must have the same shape.")

    if v1.size == 0:
        raise ValueError("Vectors cannot be empty.")

    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    if norm_v1 == 0 or norm_v2 == 0:
        raise ValueError("Vectors cannot have zero magnitude.")

    return float(np.dot(v1, v2) / (norm_v1 * norm_v2))


# Example
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])

print(round(cosine_similarity(v1, v2), 3))