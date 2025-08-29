class StructuredOutput:
    def __init__(self, model_response):
        self.model_response = model_response

    def format_output(self):
        # Format the model response into a structured format
        structured_response = {
            "response": self.model_response,
            "metadata": {
                "length": len(self.model_response.split()),
                "timestamp": self.get_timestamp()
            }
        }
        return structured_response

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

    def save_output(self, file_path):
        import json
        with open(file_path, 'w') as f:
            json.dump(self.format_output(), f, indent=4)

    def display_output(self):
        formatted = self.format_output()
        print(json.dumps(formatted, indent=4))