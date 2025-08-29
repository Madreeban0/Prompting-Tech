# File: /prompting-techniques-project/prompting-techniques-project/src/evaluation/dataset.py

class EvaluationDataset:
    def __init__(self):
        self.samples = [
            {
                "input": "What is the capital of France?",
                "expected_output": "The capital of France is Paris."
            },
            {
                "input": "Explain the theory of relativity.",
                "expected_output": "The theory of relativity, developed by Albert Einstein, describes the laws of physics in relation to observers in different frames of reference."
            },
            {
                "input": "What are the benefits of exercise?",
                "expected_output": "Exercise has numerous benefits including improved physical health, mental well-being, and increased longevity."
            },
            {
                "input": "Define machine learning.",
                "expected_output": "Machine learning is a subset of artificial intelligence that enables systems to learn from data and improve their performance over time without being explicitly programmed."
            },
            {
                "input": "What is the significance of the Turing test?",
                "expected_output": "The Turing test is a measure of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human."
            }
        ]

    def get_samples(self):
        return self.samples

    def get_sample(self, index):
        if 0 <= index < len(self.samples):
            return self.samples[index]
        else:
            raise IndexError("Sample index out of range.")