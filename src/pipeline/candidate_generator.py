import random

class CandidateGenerator:
    def generate(self, processed, pam_sites):
        seq = processed["validated_sequence"]

        candidates = []
        for i in pam_sites[:20]:
            if i + 20 < len(seq):
                candidates.append({
                    "sequence": seq[i:i+20],
                    "pam_index": i,
                    "gc": random.uniform(0.4, 0.6)
                })

        return candidates
