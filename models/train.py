from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
from joblib import dump

FEATURE_COLUMNS = [
    "molecular_weight",
    "isoelectric_point",
    "aromaticity",
    "hydrophobicity",
    "sequence_length",
    "instability_index",
    "aa_comp_A", "aa_comp_C", "aa_comp_D", "aa_comp_E",
    "aa_comp_F", "aa_comp_G", "aa_comp_H", "aa_comp_I", "aa_comp_K",
    "aa_comp_L", "aa_comp_M", "aa_comp_N", "aa_comp_P",
    "aa_comp_Q", "aa_comp_R", "aa_comp_S",
    "aa_comp_V", "aa_comp_W", "aa_comp_Y"
]


def train_svm_classifier(X_train, y_train, C = 1.0,max_iter=2000):
    # Increase allergen class weight to prioritize recall (screening use-case)
    model = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', LinearSVC(class_weight={0: 1, 1: 2},C=C, max_iter=max_iter, random_state=42))
    ])
    model.fit(X_train, y_train)
    return model

def train_logistic_regression(X_train, y_train, C = 1.0, max_iter=2000):
    # Increase allergen class weight to prioritize recall (screening use-case)
    model = Pipeline([
        ('scaler', StandardScaler()),
        ('logreg', LogisticRegression(class_weight={0: 1, 1: 2},C=C, max_iter=max_iter, random_state=42))
    ])
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    dataset = pd.read_csv('data/features/features.csv')

    X = dataset[FEATURE_COLUMNS]
    y = dataset['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    model = train_logistic_regression(X_train, y_train, C=0.5)
    
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)
