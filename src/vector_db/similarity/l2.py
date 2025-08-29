def l2_distance(embedding1, embedding2):
    """
    Calculate the L2 distance (Euclidean distance) between two embeddings.

    Parameters:
    embedding1 (list or np.array): The first embedding vector.
    embedding2 (list or np.array): The second embedding vector.

    Returns:
    float: The L2 distance between the two embeddings.
    """
    return np.sqrt(np.sum((np.array(embedding1) - np.array(embedding2)) ** 2))