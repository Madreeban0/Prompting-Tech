# File: /prompting-techniques-project/prompting-techniques-project/src/config/parameters.py

temperature = 0.7
top_p = 0.9
top_k = 50
stop_sequences = ["\n", "END"]
structured_output_format = "json"  # Options: json, xml, text
embedding_dimension = 768  # Example dimension for embeddings
vector_db_path = "path/to/vector_db"  # Path to the vector database
logging_enabled = True  # Enable or disable token logging
evaluation_samples = 5  # Number of samples for evaluation dataset
max_tokens_per_request = 150  # Maximum tokens for each AI call