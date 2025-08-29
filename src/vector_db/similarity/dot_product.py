def dot_product(embedding_a, embedding_b):
    """
    Calculate the dot product similarity between two embeddings.

    Parameters:
    embedding_a (list or np.array): The first embedding vector.
    embedding_b (list or np.array): The second embedding vector.

    Returns:
    float: The dot product similarity score.
    """
    return sum(a * b for a, b in zip(embedding_a, embedding_b))