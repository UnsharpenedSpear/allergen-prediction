# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight variant of
[Semantic Versioning](https://semver.org/) adapted for machine learning systems:

- **MAJOR** version: breaking changes to feature schema, labels, or inference API
- **MINOR** version: new models, features, or evaluation strategies
- **PATCH** version: bug fixes, refactors, documentation updates

---

## [0.4.0] – Logistic Regression Baseline Added (Current)

### Added
- Logistic Regression classifier as an alternative linear baseline
- Probability-capable model suitable for threshold tuning
- StandardScaler + LogisticRegression pipeline
- Class-weighted training (`class_weight = {0:1, 1:2}`) to prioritize allergen recall

### Evaluated
- Logistic Regression performance on held-out test set
  - Allergen recall: ~0.81
  - Allergen precision: ~0.71
  - Accuracy: ~0.88
- Performance comparable to LinearSVC with similar recall–precision tradeoff

### Notes
- Logistic Regression selected as a strong candidate for deployment due to:
  - probability outputs
  - easier threshold tuning
  - interpretability of coefficients
- Feature schema unchanged
- No degradation observed compared to SVM baseline

---

## [0.3.0] – Feature-Stable Baseline 

### Added
- Physicochemical feature: `instability_index`
- Class-weighted training for allergen class (`class_weight = {0:1, 1:2}`)
- Explicit feature schema documentation
- Initial `CHANGELOG.md`

### Changed
- Prioritized allergen recall over raw accuracy
- Updated README to reflect feature evaluation results
- Standardized feature selection using explicit column lists

### Evaluated
- Impact of `instability_index` on LinearSVC performance
  - Result: neutral impact on recall and accuracy
  - Decision: retained for future models

### Notes
- Feature schema is now considered **frozen**
- LinearSVC serves as the baseline model
- Further model experimentation should not modify feature definitions

---

## [0.2.0] – Baseline Model Training

### Added
- Linear Support Vector Classifier (LinearSVC) baseline
- Feature scaling via `StandardScaler`
- Stratified train/test split
- Classification report evaluation

### Changed
- Introduced recall-focused evaluation strategy
- Began documenting model decisions and tradeoffs

### Notes
- Accuracy alone deemed insufficient for allergen prediction
- Recall identified as primary metric

---

## [0.1.0] – Feature Engineering Pipeline

### Added
- Amino acid composition features (20 canonical residues)
- Physicochemical features:
  - molecular weight
  - isoelectric point
  - aromaticity
  - hydrophobicity
  - sequence length
- Deterministic feature extraction pipeline
- CSV-based feature dataset (`features.csv`)

### Notes
- Initial end-to-end data → feature pipeline established
- No machine learning models trained at this stage

---

## [Unreleased]

### Planned
- Logistic Regression with probability outputs
- Threshold tuning for allergen recall optimization
- ROC-AUC–based model comparison
- Random Forest baseline
- Model persistence for inference
- REST API for prediction service

---

## Changelog Policy

- Any change that affects:
  - feature schema
  - model choice
  - hyperparameters
  - evaluation metrics
  - inference behavior  
  **must be recorded in this file**
- Documentation-only changes should still be logged under PATCH updates
- Experimental results should include a brief decision rationale
