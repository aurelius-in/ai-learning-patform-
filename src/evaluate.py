import pandas as pd
from sklearn.metrics import classification_report
import joblib

def evaluate_model(data_path, model_path, vectorizer_path):
    df = pd.read_csv(data_path)
    vectorizer = joblib.load(vectorizer_path)
    model = joblib.load(model_path)
    X = vectorizer.transform(df['description'])
    y_true = df['label']
    y_pred = model.predict(X)
    
    report = classification_report(y_true, y_pred)
    print(report)

if __name__ == "__main__":
    evaluate_model("data/raw/raw_claims_data.csv", "models/checkpoints/claims_classifier.joblib", "models/checkpoints/tfidf_vectorizer.joblib")