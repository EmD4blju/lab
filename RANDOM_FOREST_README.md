# Random Forest Iris Classifier

This directory contains scripts for training and using a Random Forest classifier on the Iris dataset.

## Files

- `train_model.py` - Script to train the Random Forest model
- `predict.py` - Script to make predictions using the trained model
- `model.pkl` - Trained model and scaler (generated, not tracked in git)
- `metrics.json` - Model performance metrics (generated, not tracked in git)

## Requirements

The required dependencies are specified in `pyproject.toml`:
- scikit-learn >= 1.5.2
- joblib >= 1.4.2

Install them with:
```bash
pip install scikit-learn joblib
```

## Usage

### 1. Train the Model

Run the training script to train a Random Forest model on the Iris dataset:

```bash
python train_model.py
```

This will:
- Load the Iris dataset from scikit-learn
- Preprocess the data using StandardScaler
- Split into training (70%) and testing (30%) sets
- Train a Random Forest classifier
- Evaluate the model using multiple metrics:
  - Accuracy Score
  - Precision Score
  - Recall Score
  - F2 Score
  - ROC AUC Score
- Save the trained model to `model.pkl`
- Save the metrics to `metrics.json`

### 2. Make Predictions

After training, use the prediction script to classify your own samples:

```bash
python predict.py
```

The script will:
- Load the trained model
- Prompt you to enter values for the 4 iris features:
  1. Sepal length (cm)
  2. Sepal width (cm)
  3. Petal length (cm)
  4. Petal width (cm)
- Display the predicted class and probabilities for each class
- Allow you to make multiple predictions (type 'quit' to exit)

### Example

```
$ python predict.py
Loading model...

============================================================
Random Forest Iris Classifier - Prediction Tool
============================================================

Feature descriptions:
  1. sepal length (cm)
  2. sepal width (cm)
  3. petal length (cm)
  4. petal width (cm)

Target classes:
  0. setosa
  1. versicolor
  2. virginica
============================================================

------------------------------------------------------------
Enter sample features (or 'quit' to exit):
  sepal length (cm): 5.1
  sepal width (cm): 3.5
  petal length (cm): 1.4
  petal width (cm): 0.2

============================================================
PREDICTION RESULTS:
============================================================
Input features: [5.1, 3.5, 1.4, 0.2]

Predicted class: setosa (class 0)

Prediction probabilities:
  setosa: 1.0000 (100.00%)
  versicolor: 0.0000 (0.00%)
  virginica: 0.0000 (0.00%)
============================================================
```

## Model Performance

After training, check `metrics.json` for detailed performance metrics. Typical results:
- Accuracy: ~89%
- Precision: ~90%
- Recall: ~89%
- F2 Score: ~89%
- ROC AUC Score: ~99%

## Technical Details

- **Algorithm**: Random Forest with 100 estimators and max depth of 5
- **Preprocessing**: StandardScaler for feature normalization
- **Train/Test Split**: 70/30 with stratification to maintain class distribution
- **Multi-class Metrics**: Uses weighted averaging for precision, recall, F2, and ROC AUC
