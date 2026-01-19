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
