from src.features.physiochemical import physiochemical_features
from src.features.aa_composition import aa_composition as amino_acid_composition_features
import csv

FEATURE_COLUMNS = [
    "molecular_weight",
    "isoelectric_point",
    "aromaticity",
    "hydrophobicity",
    "sequence_length",
    "aa_A","aa_C","aa_D","aa_E","aa_F","aa_G","aa_H","aa_I","aa_K","aa_L",
    "aa_M","aa_N","aa_P","aa_Q","aa_R","aa_S","aa_T","aa_V","aa_W","aa_Y"
]


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