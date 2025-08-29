def generate_embedding(embedding_model, text):
    """
    Generates an embedding for the given text using the specified embedding model.

    Parameters:
    embedding_model: The model used to generate embeddings.
    text (str): The input text for which to generate the embedding.

    Returns:
    numpy.ndarray: The generated embedding.
    """
    return embedding_model.encode(text)

def load_embeddings(file_path):
    """
    Loads embeddings from a specified file.

    Parameters:
    file_path (str): The path to the file containing embeddings.

    Returns:
    dict: A dictionary mapping text to its corresponding embedding.
    """
    import numpy as np
    import json

    with open(file_path, 'r') as f:
        data = json.load(f)
    
    embeddings = {item['text']: np.array(item['embedding']) for item in data}
    return embeddings

def save_embeddings(embeddings, file_path):
    """
    Saves embeddings to a specified file.

    Parameters:
    embeddings (dict): A dictionary mapping text to its corresponding embedding.
    file_path (str): The path to the file where embeddings will be saved.
    """
    import json

    data = [{'text': text, 'embedding': embedding.tolist()} for text, embedding in embeddings.items()]
    with open(file_path, 'w') as f:
        json.dump(data, f)

def normalize_embedding(embedding):
    """
    Normalizes the given embedding.

    Parameters:
    embedding (numpy.ndarray): The embedding to normalize.

    Returns:
    numpy.ndarray: The normalized embedding.
    """
    norm = np.linalg.norm(embedding)
    if norm == 0:
        return embedding
    return embedding / norm

def calculate_similarity(embedding1, embedding2, method='cosine'):
    """
    Calculates the similarity between two embeddings using the specified method.

    Parameters:
    embedding1 (numpy.ndarray): The first embedding.
    embedding2 (numpy.ndarray): The second embedding.
    method (str): The similarity method to use ('cosine', 'l2', or 'dot_product').

    Returns:
    float: The calculated similarity score.
    """
    if method == 'cosine':
        from sklearn.metrics.pairwise import cosine_similarity
        return cosine_similarity([embedding1], [embedding2])[0][0]
    elif method == 'l2':
        return np.linalg.norm(embedding1 - embedding2)
    elif method == 'dot_product':
        return np.dot(embedding1, embedding2)
    else:
        raise ValueError("Unknown similarity method: {}".format(method))