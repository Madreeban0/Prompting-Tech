from unittest import TestCase
from src.evaluation.dataset import EvaluationDataset
from src.prompting.zero_shot import zero_shot_prompt
from src.prompting.one_shot import one_shot_prompt
from src.prompting.multi_shot import multi_shot_prompt
from src.prompting.dynamic import dynamic_prompt
from src.prompting.chain_of_thought import chain_of_thought_prompt

class TestPromptingTechniques(TestCase):
    def setUp(self):
        self.dataset = EvaluationDataset()
        self.samples = self.dataset.get_samples()

    def test_zero_shot(self):
        for sample in self.samples:
            prompt = zero_shot_prompt(sample['input'])
            self.assertIsNotNone(prompt)
            self.assertIn('expected_output', sample)
            self.assertEqual(prompt, sample['expected_output'])

    def test_one_shot(self):
        for sample in self.samples:
            prompt = one_shot_prompt(sample['input'], sample['example'])
            self.assertIsNotNone(prompt)
            self.assertIn('expected_output', sample)
            self.assertEqual(prompt, sample['expected_output'])

    def test_multi_shot(self):
        for sample in self.samples:
            prompt = multi_shot_prompt(sample['input'], sample['examples'])
            self.assertIsNotNone(prompt)
            self.assertIn('expected_output', sample)
            self.assertEqual(prompt, sample['expected_output'])

    def test_dynamic(self):
        previous_output = None
        for sample in self.samples:
            prompt = dynamic_prompt(sample['input'], previous_output)
            self.assertIsNotNone(prompt)
            previous_output = prompt
            self.assertIn('expected_output', sample)
            self.assertEqual(prompt, sample['expected_output'])

    def test_chain_of_thought(self):
        for sample in self.samples:
            prompt = chain_of_thought_prompt(sample['input'])
            self.assertIsNotNone(prompt)
            self.assertIn('expected_output', sample)
            self.assertEqual(prompt, sample['expected_output'])

if __name__ == '__main__':
    unittest.main()