def generate_zero_shot_prompt(input_text):
    """
    Generates a prompt using the zero-shot prompting technique.
    
    Parameters:
    input_text (str): The input text for which a prompt is to be generated.
    
    Returns:
    str: The generated prompt.
    """
    prompt = f"Given the following input: '{input_text}', generate a relevant response without any prior examples."
    return prompt

if __name__ == "__main__":
    # Example usage
    input_text = "What are the benefits of using renewable energy?"
    prompt = generate_zero_shot_prompt(input_text)
    print(prompt)