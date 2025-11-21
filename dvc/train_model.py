"""
Train a Random Forest classifier on the Iris dataset and save the model and metrics.
"""
import json
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    fbeta_score,
    roc_auc_score
)
import numpy as np


def main():
    # Load the Iris dataset
    print("Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Simple preprocessing: standardize features
    print("Preprocessing data...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split the dataset into training and testing sets
    print("Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Train Random Forest model
    print("Training Random Forest model...")
    rf_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        max_depth=5
    )
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    print("Making predictions...")
    y_pred = rf_model.predict(X_test)
    y_pred_proba = rf_model.predict_proba(X_test)
    
    # Calculate metrics
    print("Calculating metrics...")
    
    # For multi-class classification, we need to specify averaging strategy
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f2 = fbeta_score(y_test, y_pred, beta=2, average='weighted')
    
    # For ROC AUC with multi-class, we use one-vs-rest and macro averaging
    roc_auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr', average='weighted')
    
    # Store metrics in a dictionary
    metrics = {
        'accuracy_score': float(accuracy),
        'precision_score': float(precision),
        'recall_score': float(recall),
        'f2_score': float(f2),
        'roc_auc_score': float(roc_auc)
    }
    
    # Print metrics
    print("\n" + "=" * 50)
    print("Model Performance Metrics:")
    print("=" * 50)
    for metric_name, metric_value in metrics.items():
        print(f"{metric_name}: {metric_value:.4f}")
    print("=" * 50 + "\n")
    
    # Save metrics to JSON file
    print("Saving metrics to metrics.json...")
    with open('dvc/models/rf/metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    
    # Save the model and scaler to PKL file using joblib
    print("Saving model and scaler to model.pkl...")
    model_data = {
        'model': rf_model,
        'scaler': scaler,
        'feature_names': iris.feature_names,
        'target_names': iris.target_names.tolist()
    }
    joblib.dump(model_data, 'dvc/models/rf/model.pkl')
    
    print("\nTraining complete!")
    print(f"Model saved to: model.pkl")
    print(f"Metrics saved to: metrics.json")


if __name__ == "__main__":
    main()
