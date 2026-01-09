# allergen-prediction/data/build_dataset.py
from Bio import SeqIO
import csv

MIN_LENGTH = 30
MAX_LENGTH = 2000

AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")

ALLERGEN = 1
NON_ALLERGEN = 0

def is_valid_sequence(seq: str):
    """
    Check if a protein sequence is valid based on length and allowed amino acids.

    Args:
        seq (str): Protein sequence.

    Returns:
        str or None: Cleaned sequence if valid, else None.
    """
    seq = str(seq).upper()
    seq = seq.strip()
    if not (MIN_LENGTH <= len(seq) <= MAX_LENGTH):
        return None
    if not set(seq).issubset(AMINO_ACIDS):
        return None
    return seq

def parse(fasta_file: str) -> list:
    """Parse a FASTA file and return a list of sequences.

    Args:
        fasta_file (str): Path to the FASTA file.

    Returns:
        list: List of sequences.
    """
    sequences = []
    with open(fasta_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
                sequences.append(record.seq)
    return sequences

def clean_sequences(sequences: list) -> list:
    """
    Clean a list of protein sequences.

    Args:
        sequences (list): List of protein sequences.

    Returns:
        list: List of cleaned and valid protein sequences.
    """

    cleaned = []
    for seq in sequences:
        valid_seq = is_valid_sequence(seq)
        if valid_seq:
            cleaned.append(valid_seq)
    return list(set(cleaned))




if __name__ == "__main__":
    raw_allergen_seqs = parse("data/raw/allergen.fasta")
    raw_non_allergen_seqs = parse("data/raw/non_allergen.fasta")

    cleaned_allergen_seqs = clean_sequences(raw_allergen_seqs)
    cleaned_non_allergen_seqs = clean_sequences(raw_non_allergen_seqs)

    dataset = []
    for seq in cleaned_allergen_seqs:
        dataset.append((str(seq), ALLERGEN))
    for seq in cleaned_non_allergen_seqs:
        dataset.append((str(seq), NON_ALLERGEN))

    with open("data/processed/dataset.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["sequence", "label"])
        writer.writerows(dataset)