def validate_dna(seq: str) -> str:
    """Basic DNA cleaning"""
    return seq.upper().replace(" ", "").replace("\n", "")


def reverse_complement(seq: str) -> str:
    mapping = str.maketrans("ATGC", "TACG")
    return seq.translate(mapping)[::-1]
