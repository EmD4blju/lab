"""
Load a trained Random Forest model and make predictions on user-provided samples.
"""
import joblib
import numpy as np


def main():
    # Load the trained model and scaler
    print("Loading model...")
    try:
        model_data = joblib.load('dvc/models/model.pkl')
        model = model_data['model']
        scaler = model_data['scaler']
        feature_names = model_data['feature_names']
        target_names = model_data['target_names']
    except FileNotFoundError:
        print("Error: model.pkl not found. Please run train_model.py first.")
        return
    
    print("\n" + "=" * 60)
    print("Random Forest Iris Classifier - Prediction Tool")
    print("=" * 60)
    print("\nFeature descriptions:")
    for i, name in enumerate(feature_names, 1):
        print(f"  {i}. {name}")
    print("\nTarget classes:")
    for i, name in enumerate(target_names):
        print(f"  {i}. {name}")
    print("=" * 60)
    
    while True:
        print("\n" + "-" * 60)
        print("Enter sample features (or 'quit' to exit):")
        
        sample = []
        for feature_name in feature_names:
            while True:
                try:
                    user_input = input(f"  {feature_name}: ").strip()
                    if user_input.lower() == 'quit':
                        print("\nExiting...")
                        return
                    value = float(user_input)
                    sample.append(value)
                    break
                except ValueError:
                    print("    Invalid input. Please enter a numeric value.")
        
        # Convert to numpy array and reshape
        sample_array = np.array(sample).reshape(1, -1)
        
        # Apply the same preprocessing (scaling)
        sample_scaled = scaler.transform(sample_array)
        
        # Make prediction
        prediction = model.predict(sample_scaled)[0]
        prediction_proba = model.predict_proba(sample_scaled)[0]
        
        # Display results
        print("\n" + "=" * 60)
        print("PREDICTION RESULTS:")
        print("=" * 60)
        print(f"Input features: {sample}")
        print(f"\nPredicted class: {target_names[prediction]} (class {prediction})")
        print("\nPrediction probabilities:")
        for i, (class_name, prob) in enumerate(zip(target_names, prediction_proba)):
            print(f"  {class_name}: {prob:.4f} ({prob*100:.2f}%)")
        print("=" * 60)


if __name__ == "__main__":
    main()
