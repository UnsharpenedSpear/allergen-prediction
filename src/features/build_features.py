from features.physiochemical import physiochemical_features
from features.aa_composition import amino_acid_composition_features
import csv

def build_feature_dataframe(input_csv: str, output_csv: str) -> None:
    """Build feature dataframe from input CSV and save to output CSV."""
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        fieldnames = reader.fieldnames + [
            'molecular_weight', 'isoelectric_point', 'aromaticity',
            'hydrophobicity', 'sequence_length'
        ] + [f'aa_comp_{aa}' for aa in "ACDEFGHIKLMNPQRSTVWY"]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            sequence = row['sequence']
            physio_features = physiochemical_features(sequence)
            aa_comp_features = amino_acid_composition_features(sequence)
            row.update(physio_features)
            row.update({f'aa_comp_{k}': v for k, v in aa_comp_features.items()})
            writer.writerow(row)