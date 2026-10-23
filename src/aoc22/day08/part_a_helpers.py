import numpy as np

def get_viewing_distance(height, trees):
    trees = np.asarray(trees)
    return np.argmax(trees >= height) + 1 if np.any(trees >= height) else len(trees)
