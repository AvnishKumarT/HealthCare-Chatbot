
# Logic to process symptoms and provide remedies
import pandas as pd

class SymptomMatcher:
    def __init__(self, dataset_path):
        self.dataset = pd.read_csv(dataset_path)

    def match_symptom(self, user_input):
        for _, row in self.dataset.iterrows():
            if row['Symptom'].lower() in user_input.lower():
                return row['Suggestion']
        return "Consult a healthcare professional."
