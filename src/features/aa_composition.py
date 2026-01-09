AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

def aa_composition(sequence: str) -> dict:
    """Calculate the amino acid composition of a protein sequence.

    Args:
        sequence (str): Protein sequence.

    Returns:
        dict: A dictionary with amino acids as keys and their
              corresponding frequencies as values.
    """
    composition = {aa: 0 for aa in AMINO_ACIDS}
    seq_length = len(sequence)

    for aa in sequence:
        if aa in composition:
            composition[aa] += 1

    for aa in composition:
        composition[aa] /= seq_length

    return composition
