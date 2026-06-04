import random

class PINNModel:
    def predict(self, sequence: str, context: str):
        return {
            "specificity": random.uniform(0.5, 0.9),
            "cfd": random.uniform(0.1, 0.3),
            "deltaG": random.uniform(-27, -24),
            "mfe": random.uniform(-3, 0),
            "gc": random.uniform(0.4, 0.6)
        }
