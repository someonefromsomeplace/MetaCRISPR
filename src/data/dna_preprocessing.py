from utils.sequence_utils import validate_dna

class DNAProcessor:
    def process(self, dna_sequence: str):
        clean_seq = validate_dna(dna_sequence)

        # mock windowing
        windows = [
            clean_seq[i:i+100]
            for i in range(0, len(clean_seq)-100, 50)
        ]

        return {
            "validated_sequence": clean_seq,
            "windows": windows
        }
