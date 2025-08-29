# main.py

import sys
from prompting.zero_shot import generate_zero_shot_prompt
from prompting.one_shot import generate_one_shot_prompt
from prompting.multi_shot import generate_multi_shot_prompt
from prompting.dynamic import generate_dynamic_prompt
from prompting.chain_of_thought import generate_chain_of_thought_prompt
from evaluation.dataset import load_evaluation_dataset
from evaluation.metrics import evaluate_model
from testing.test_framework import run_tests
from logging.token_logger import TokenLogger
from config.parameters import get_parameters
from output.structured_output import format_output
from function_calling.function_caller import call_function
from embeddings.embedding_utils import generate_embeddings
from vector_db.vector_database import VectorDatabase

def main():
    # Load configuration parameters
    params = get_parameters()
    
    # Initialize token logger
    token_logger = TokenLogger()
    
    # Load evaluation dataset
    dataset = load_evaluation_dataset()
    
    # Initialize vector database
    vector_db = VectorDatabase()
    
    # Example usage of prompting techniques
    prompt = generate_zero_shot_prompt("What is the capital of France?")
    print(format_output(prompt))
    
    prompt = generate_one_shot_prompt("Translate 'Hello' to French.", example="Hello: Bonjour")
    print(format_output(prompt))
    
    prompt = generate_multi_shot_prompt("Translate 'Goodbye' to French.", examples=[("Hello", "Bonjour"), ("Thank you", "Merci")])
    print(format_output(prompt))
    
    prompt = generate_dynamic_prompt("What is the weather like today?")
    print(format_output(prompt))
    
    prompt = generate_chain_of_thought_prompt("If I have 2 apples and I give away 1, how many do I have left?")
    print(format_output(prompt))
    
    # Evaluate model performance
    results = evaluate_model(dataset)
    print("Evaluation Results:", results)
    
    # Run tests
    run_tests()
    
    # Log token usage
    token_logger.log_usage()
    
    # Example of function calling
    result = call_function("example_function", args={"param1": "value1"})
    print("Function Call Result:", result)

if __name__ == "__main__":
    main()