# Prompting-Tech: Advanced Prompting Techniques Framework

A comprehensive Python framework demonstrating various prompting techniques for Large Language Models (LLMs) with integrated evaluation, testing, and vector database capabilities.

## 📋 Overview

Prompting-Tech is a modular and extensible framework designed to help developers understand, implement, and evaluate different prompting techniques for AI language models. This project provides practical implementations of industry-standard prompting strategies, complete with evaluation metrics, testing frameworks, and supporting infrastructure.

## ✨ Features

- **Multiple Prompting Techniques**: Implementations of various prompting strategies including:
  - Zero-Shot Prompting
  - One-Shot Prompting
  - Multi-Shot (Few-Shot) Prompting
  - Dynamic Prompting
  - Chain of Thought Prompting

- **Evaluation Framework**: Built-in dataset and metrics for assessing model performance
- **Testing Infrastructure**: Comprehensive test framework for validating prompting techniques
- **Vector Database**: Integration with vector databases for semantic search and similarity matching
- **Function Calling**: Support for dynamic function execution based on prompts
- **Embeddings Support**: Utilities for generating, storing, and manipulating text embeddings
- **Structured Output**: Formatting utilities for consistent model response handling
- **Token Logging**: Track and monitor token usage across different prompting techniques
- **Configuration Management**: Centralized parameter management system

## 🏗️ Project Structure

```
Prompting-Tech/
├── src/
│   ├── main.py                    # Main application entry point
│   ├── prompting/                 # Prompting technique implementations
│   │   ├── zero_shot.py          # Zero-shot prompting
│   │   ├── one_shot.py           # One-shot prompting
│   │   ├── multi_shot.py         # Multi-shot (few-shot) prompting
│   │   ├── dynamic.py            # Dynamic prompting
│   │   └── chain_of_thought.py   # Chain of thought prompting
│   ├── evaluation/                # Model evaluation components
│   │   ├── dataset.py            # Evaluation dataset loader
│   │   └── metrics.py            # Performance metrics
│   ├── testing/                   # Testing framework
│   │   └── test_framework.py     # Test execution and validation
│   ├── vector_db/                 # Vector database implementation
│   │   └── vector_database.py    # Vector storage and similarity search
│   ├── embeddings/                # Embedding utilities
│   │   └── embedding_utils.py    # Generate and manipulate embeddings
│   ├── function_calling/          # Function calling support
│   │   └── function_caller.py    # Dynamic function execution
│   ├── output/                    # Output formatting
│   │   └── structured_output.py  # Response formatting utilities
│   ├── logging/                   # Logging infrastructure
│   │   └── token_logger.py       # Token usage tracking
│   ├── config/                    # Configuration management
│   │   └── parameters.py         # Parameter configuration
│   └── video_explanations/        # Documentation and explanations
│       ├── zero_shot.md
│       ├── one_shot.md
│       ├── multi_shot.md
│       ├── dynamic.md
│       ├── chain_of_thought.md
│       ├── testing.md
│       ├── evaluation.md
│       ├── embeddings.md
│       ├── vector_db.md
│       ├── function_calling.md
│       ├── output.md
│       ├── logging.md
│       ├── config.md
│       └── similarity.md
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Madreeban0/Prompting-Tech.git
cd Prompting-Tech
```

2. Install required dependencies:
```bash
pip install numpy scikit-learn
```

### Basic Usage

Run the main application to see all prompting techniques in action:

```bash
python src/main.py
```

## 💡 Prompting Techniques Explained

### Zero-Shot Prompting
Zero-shot prompting allows the model to perform tasks without any prior examples. The model relies solely on its pre-trained knowledge and the prompt context.

**Example:**
```python
from prompting.zero_shot import generate_zero_shot_prompt

prompt = generate_zero_shot_prompt("What is the capital of France?")
print(prompt)
```

### One-Shot Prompting
One-shot prompting provides a single example to guide the model's response format and style.

**Example:**
```python
from prompting.one_shot import generate_one_shot_prompt

prompt = generate_one_shot_prompt(
    "Translate 'Hello' to French.", 
    example="Hello: Bonjour"
)
print(prompt)
```

### Multi-Shot (Few-Shot) Prompting
Multi-shot prompting provides multiple examples to establish a pattern for the model to follow.

**Example:**
```python
from prompting.multi_shot import generate_multi_shot_prompt

prompt = generate_multi_shot_prompt(
    "Translate 'Goodbye' to French.",
    examples=[("Hello", "Bonjour"), ("Thank you", "Merci")]
)
print(prompt)
```

### Dynamic Prompting
Dynamic prompting adapts based on context or previous interactions, enabling more contextual responses.

**Example:**
```python
from prompting.dynamic import generate_dynamic_prompt

prompt = generate_dynamic_prompt("What is the weather like today?")
print(prompt)
```

### Chain of Thought Prompting
Chain of thought prompting encourages the model to show its reasoning process step-by-step, improving accuracy on complex tasks.

**Example:**
```python
from prompting.chain_of_thought import generate_chain_of_thought_prompt

prompt = generate_chain_of_thought_prompt(
    "If I have 2 apples and I give away 1, how many do I have left?"
)
print(prompt)
```

## 🧪 Evaluation and Testing

The framework includes built-in evaluation capabilities:

```python
from evaluation.dataset import load_evaluation_dataset
from evaluation.metrics import evaluate_model

# Load evaluation dataset
dataset = load_evaluation_dataset()

# Evaluate model performance
results = evaluate_model(dataset)
print("Evaluation Results:", results)
```

Run tests to validate the implementation:

```python
from testing.test_framework import run_tests

run_tests()
```

## 🔧 Advanced Features

### Vector Database Integration

Store and retrieve embeddings for semantic search:

```python
from vector_db.vector_database import VectorDatabase

vector_db = VectorDatabase()
vector_db.add_embedding([0.1, 0.2, 0.3], id="doc1")
similar = vector_db.find_most_similar([0.15, 0.25, 0.35], top_k=5)
```

### Embeddings Utilities

Generate and manage text embeddings:

```python
from embeddings.embedding_utils import generate_embeddings

embeddings = generate_embeddings(text="Your text here")
```

### Function Calling

Execute functions dynamically based on prompts:

```python
from function_calling.function_caller import call_function

result = call_function("example_function", args={"param1": "value1"})
```

### Structured Output Formatting

Format model responses consistently:

```python
from output.structured_output import format_output

formatted = format_output(response)
```

## 📊 Token Logging

Monitor and track token usage across different prompting techniques:

```python
from logging.token_logger import TokenLogger

token_logger = TokenLogger()
token_logger.log_usage()
```

## 🎓 Learning Resources

Each prompting technique includes detailed video explanations in the `src/video_explanations/` directory. These markdown files provide:

- Comprehensive overviews
- Use cases and applications
- Implementation details
- Advantages and limitations
- Practical demonstrations

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational and research purposes.

## 🙏 Acknowledgments

- Inspired by research in prompt engineering and LLM optimization
- Built with modularity and extensibility in mind
- Designed for both learning and production use cases

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub.

---

**Happy Prompting! 🎯**
