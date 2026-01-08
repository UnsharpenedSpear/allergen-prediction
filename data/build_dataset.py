# allergen-prediction/data/build_dataset.py
from Bio import SeqIO
import csv

VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")
MIN_LENGTH = 30
MAX_LENGTH = 2000

ALLERGEN = 1
NON_ALLERGEN = 0

def is_valid_sequence(seq):
    seq = str(seq).upper()
    seq = seq.strip()
    if not (MIN_LENGTH <= len(seq) <= MAX_LENGTH):
        return None
    if not set(seq).issubset(VALID_AA):
        return None
    return seq

def parse(fasta_file):
    sequences = []
    with open(fasta_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
                sequences.append(record.seq)
    return sequences

def clean_sequences(sequences):
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