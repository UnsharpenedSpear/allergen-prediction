from Bio.SeqUtils import molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def physiochemical_features(sequence: str) -> dict[str, float]:
    """Calculate physiochemical features of a protein sequence.

    Args:
        sequence (str): Protein sequence.

    Returns:
        dict[str, float]: A dictionary containing molecular weight,
                          isoelectric point, aromaticity, instability index and hydrophobicity.
    """
    analysis = ProteinAnalysis(sequence)
    features = {
        "molecular_weight": molecular_weight(sequence),
        "isoelectric_point": analysis.isoelectric_point(),
        "aromaticity": analysis.aromaticity(),
        "instability_index": analysis.instability_index(),
        "hydrophobicity": analysis.gravy(),
    }
    
    return features