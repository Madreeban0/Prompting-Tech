def generate_multi_shot_prompting(examples, user_input):
    """
    Generates a prompt using multiple examples to provide context for the model.

    Parameters:
    examples (list of str): A list of example prompts and their corresponding responses.
    user_input (str): The input from the user for which a response is to be generated.

    Returns:
    str: A constructed prompt that includes the examples and the user input.
    """
    prompt = "Here are some examples of how to respond:\n"
    for example in examples:
        prompt += f"- {example}\n"
    prompt += f"Now, based on these examples, respond to the following input:\n{user_input}"
    return prompt

# Example usage
if __name__ == "__main__":
    examples = [
        "Example 1: What is the capital of France? Response: The capital of France is Paris.",
        "Example 2: What is the largest planet in our solar system? Response: The largest planet is Jupiter.",
        "Example 3: Who wrote 'Hamlet'? Response: 'Hamlet' was written by William Shakespeare."
    ]
    user_input = "What is the smallest planet in our solar system?"
    prompt = generate_multi_shot_prompting(examples, user_input)
    print(prompt)