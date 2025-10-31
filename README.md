# Prompting Tech

A comprehensive Python library for implementing and demonstrating various prompting techniques used in Large Language Models (LLMs) and AI applications. This project provides modular implementations of different prompting strategies, evaluation metrics, vector database operations, and testing frameworks.

## Overview

Prompting Tech is designed to help developers understand and implement advanced prompting techniques for AI systems. The library includes practical implementations of zero-shot, one-shot, multi-shot, chain-of-thought, and dynamic prompting methods, along with supporting infrastructure for evaluation, logging, and function calling.

## Features

### Prompting Techniques
- **Zero-Shot Prompting**: Generate responses without prior examples
- **One-Shot Prompting**: Provide a single example to guide model behavior
- **Multi-Shot Prompting**: Use multiple examples for better context
- **Chain-of-Thought Prompting**: Enable step-by-step reasoning
- **Dynamic Prompting**: Adapt prompts based on context

### Core Components
- **Vector Database**: Store and retrieve embeddings with similarity search
- **Evaluation Framework**: Comprehensive metrics including accuracy, precision, recall, and F1 score
- **Token Logger**: Track and monitor token usage
- **Function Calling**: Integrate external function calls within prompting workflows
- **Structured Output**: Format and structure model outputs consistently
- **Testing Framework**: Validate prompting techniques and model performance

### Similarity Metrics
- Cosine Similarity
- L2 Distance
- Dot Product

## Installation

Clone the repository:

```bash
git clone https://github.com/Madreeban0/Prompting-Tech.git
cd Prompting-Tech
```

Install required dependencies:

```bash
pip install numpy
```

Note: Additional dependencies may be required depending on the specific features you plan to use. The core functionality requires numpy for vector operations and similarity calculations.

## Usage

### Basic Example

```python
from src.prompting.zero_shot import generate_zero_shot_prompt

# Zero-shot prompting
prompt = generate_zero_shot_prompt("What is the capital of France?")
print(prompt)
```

### Running the Main Application

```python
from src.main import main

# Run the main application to see all prompting techniques in action
main()
```

### Vector Database Operations

```python
from src.vector_db.vector_database import VectorDatabase
from src.embeddings.embedding_utils import generate_embeddings

# Initialize vector database
vector_db = VectorDatabase()

# Add embeddings
embedding = [0.1, 0.2, 0.3, 0.4]
vector_db.add_embedding(embedding, id="doc1")

# Find similar vectors
query_embedding = [0.15, 0.25, 0.35, 0.45]
results = vector_db.find_most_similar(query_embedding, top_k=5)
```

### Model Evaluation

```python
from src.evaluation.metrics import evaluate_model

# Example predictions and labels
predictions = [1, 0, 1, 1, 0]
labels = [1, 0, 1, 0, 0]

# Evaluate model performance
results = evaluate_model(predictions, labels)
print(results)
```

## Project Structure

```
Prompting-Tech/
├── src/
│   ├── main.py                      # Main entry point
│   ├── prompting/                   # Prompting techniques
│   │   ├── zero_shot.py
│   │   ├── one_shot.py
│   │   ├── multi_shot.py
│   │   ├── chain_of_thought.py
│   │   └── dynamic.py
│   ├── evaluation/                  # Evaluation tools
│   │   ├── dataset.py
│   │   └── metrics.py
│   ├── testing/                     # Testing framework
│   │   └── test_framework.py
│   ├── logging/                     # Token logging
│   │   └── token_logger.py
│   ├── config/                      # Configuration
│   │   └── parameters.py
│   ├── output/                      # Output formatting
│   │   └── structured_output.py
│   ├── function_calling/            # Function calling utilities
│   │   └── function_caller.py
│   ├── embeddings/                  # Embedding utilities
│   │   └── embedding_utils.py
│   ├── vector_db/                   # Vector database
│   │   ├── vector_database.py
│   │   └── similarity/
│   │       ├── cosine.py
│   │       ├── l2.py
│   │       └── dot_product.py
│   └── video_explanations/          # Educational documentation
│       ├── zero_shot.md
│       ├── one_shot.md
│       ├── multi_shot.md
│       ├── chain_of_thought.md
│       ├── dynamic.md
│       ├── embeddings.md
│       ├── vector_db.md
│       ├── function_calling.md
│       ├── evaluation.md
│       ├── testing.md
│       ├── logging.md
│       ├── config.md
│       ├── output.md
│       └── similarity.md
└── README.md
```

## Running the Application

Execute the main application:

```bash
python src/main.py
```

This will demonstrate various prompting techniques, evaluate model performance, run tests, and log token usage.

## Contributing

Contributions are welcome. Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes with clear commit messages
4. Test your changes thoroughly
5. Submit a pull request with a detailed description

## License

This project is available for educational and research purposes. Please refer to the repository for specific license terms.

## Documentation

Detailed explanations of each component are available in the `src/video_explanations/` directory:

- Zero-Shot Prompting
- One-Shot Prompting
- Multi-Shot Prompting
- Chain-of-Thought Prompting
- Dynamic Prompting
- Embeddings
- Vector Database
- Function Calling
- Evaluation Metrics
- Testing Framework
- Logging
- Configuration
- Output Formatting
- Similarity Metrics

## Contact

For questions or suggestions, please open an issue on the GitHub repository.
