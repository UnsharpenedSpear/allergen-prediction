from src.features.build_features import build_feature_dataframe

build_feature_dataframe(
    "data/processed/cleaned_sequences.csv",
    "data/features/features.csv"
)
