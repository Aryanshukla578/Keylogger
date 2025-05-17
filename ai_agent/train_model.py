import joblib
import os
import numpy as np

class BehaviorAnalyzer:
    def __init__(self, model_path="zerotrace/ai_agent/model.pkl"):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        self.model = joblib.load(model_path)

    def extract_features(self, payload: str) -> np.ndarray:
        # Simple handcrafted features from payload text
        features = []

        # Feature 1: Length of payload
        features.append(len(payload))

        # Feature 2: Count of special characters
        special_chars = ['<', '>', '"', "'", '=', '(', ')', ';', '{', '}', '%']
        special_count = sum(payload.count(char) for char in special_chars)
        features.append(special_count)

        # Feature 3: Keyword presence score (e.g., SQLi/XSS indicators)
        keywords = ['select', 'insert', 'script', 'alert', 'drop', 'onerror', 'eval']
        keyword_score = sum(payload.lower().count(kw) for kw in keywords)
        features.append(keyword_score)

        # Feature 4: Ratio of digits to characters
        digit_ratio = sum(c.isdigit() for c in payload) / max(len(payload), 1)
        features.append(digit_ratio)

        return np.array(features).reshape(1, -1)

    def predict(self, payload: str) -> str:
        features = self.extract_features(payload)
        prediction = self.model.predict(features)[0]
        return "Malicious" if prediction == 1 else "Benign"
