import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    den = np.linalg.norm(a) * np.linalg.norm(b)
    if den == 0:
        return 0

    # Write code here
    return np.dot(a,b)/den