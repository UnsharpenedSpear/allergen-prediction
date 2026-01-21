# Allergen Prediction Web Service

## Overview

This project implements a **protein allergen prediction pipeline** that combines bioinformatics feature engineering with classical machine learning. Given a protein amino acid sequence, the system extracts biologically meaningful features and predicts whether the protein is likely to be an allergen.

The project is designed as an **end-to-end ML system**, covering:
- sequence preprocessing
- deterministic feature extraction
- supervised model training
- evaluation using domain-appropriate metrics
- preparation for deployment as a web service

The focus is on **interpretability, reproducibility, and deployability**, rather than deep learning.

---

## Problem Definition

- **Task:** Binary classification  
- **Input:** Protein amino acid sequence  
- **Output:**  
  - `1` → Allergen  
  - `0` → Non-allergen  

### Domain Consideration

In allergen prediction, **false negatives are more costly than false positives**.  
Missing an allergen is worse than flagging a non-allergen, so **recall for the allergen class is prioritized** over raw accuracy.

---

## Project Structure

```text
allergen-prediction/
├── data/
│   ├── raw/                 # Original downloaded sequence data
│   ├── processed/           # Cleaned and labeled sequences
│   └── features/            # Final ML-ready feature matrix
│       └── features.csv
├── src/
│   ├── features/            # Feature engineering modules
│   │   ├── aa_composition.py
│   │   ├── physicochemical.py
│   │   └── build_features.py
│   ├── models/              # Model training and inference code
│   └── app/                 # (Planned) API layer
├── tests/                   # Unit and integration tests
├── models/                  # Saved trained models
├── notebooks/               # Exploratory analysis (optional)
└── README.md
```
---

## Feature Engineering

Each protein sequence is converted into a fixed-length numeric feature vector suitable for classical machine learning models.

### Feature Schema (Frozen)

Total features: 27

### Physicochemical Features

- molecular_weight
- isoelectric_point
- aromaticity
- hydrophobicity
- instability_index
- sequence_length

These global descriptors capture size, charge, hydrophobicity, aromatic content, and predicted structural stability of the protein.

The instability index was included as a protein stability descriptor.  
In initial LinearSVC experiments, its inclusion did not significantly change performance, but it was retained because it may benefit other classifiers.

---

### Amino Acid Composition

Fractional frequency of each amino acid in the sequence:

- aa_comp_A, aa_comp_C, aa_comp_D, aa_comp_E, aa_comp_F
- aa_comp_G, aa_comp_H, aa_comp_I, aa_comp_K, aa_comp_L
- aa_comp_M, aa_comp_N, aa_comp_P, aa_comp_Q, aa_comp_R
- aa_comp_S, aa_comp_T, aa_comp_V, aa_comp_W, aa_comp_Y

---

### Design Principles

- Deterministic feature extraction
- Alignment-free representation
- No external databases required at inference time
- Suitable for real-time API usage
- Explicit feature ordering to prevent schema drift

---

## Machine Learning Models

### Baseline Model

Linear Support Vector Classifier (LinearSVC)

- Feature scaling using StandardScaler
- 80/20 stratified train-test split
- Fixed random seed for reproducibility
- Implemented via a scikit-learn Pipeline

---

### Handling Class Imbalance

Initial experiments showed reduced recall for allergens due to class imbalance.  
To address this, class-weighted training was introduced:

- class_weight = {0: 1, 1: 2}


This explicitly prioritizes allergen recall, consistent with the screening nature of the task.

---

## Model Performance

Evaluation was performed on a held-out test set.

### LinearSVC Results

| Model      | Features            | Allergen Recall | Allergen Precision | Accuracy |
|-----------|---------------------|-----------------|-------------------|----------|
| LinearSVC | Base features       | 0.81            | 0.72              | 0.88     |
| LinearSVC | + instability_index | 0.80            | 0.72              | 0.88     |

---

### Interpretation

- Increasing allergen class weight significantly improved recall
- Adding instability index had neutral impact on LinearSVC performance
- Precision decreased slightly as recall increased
- Overall accuracy remained stable

Given the application domain, the recall-focused configuration is preferred.

---

## Evaluation Metrics

Primary metric:
- Allergen recall

Secondary metrics:
- Precision
- F1-score
- Accuracy

ROC-AUC and probability-based threshold tuning are planned next.

---

## Reproducibility

- Fixed random seeds
- Frozen feature schema and order
- Explicit feature column selection
- Deterministic preprocessing
- No data leakage between training and testing

---

## Current Status

- [x] Feature pipeline implemented and validated
- [x] Feature schema frozen and documented
- [x] LinearSVC baseline trained with class weighting
- [x] Instability index evaluated and retained
- [ ] Logistic Regression with probability outputs
- [ ] Threshold tuning for recall optimization
- [ ] Random Forest comparison
- [ ] Model selection and persistence
- [ ] API deployment

---

## Next Steps

1. Train Logistic Regression with scaled features
2. Evaluate ROC-AUC and allergen recall
3. Tune decision threshold to optimize recall
4. Compare with Random Forest
5. Select final model for deployment
6. Expose inference via a web API

---

## Notes

This project intentionally uses classical machine learning rather than deep learning to emphasize:
- interpretability
- computational efficiency
- ease of deployment
- suitability for small to medium biological datasets

---

## Documentation Policy

Any change that affects:
- feature schema
- model choice
- hyperparameters
- evaluation results
- inference behavior

must be documented in this README.
