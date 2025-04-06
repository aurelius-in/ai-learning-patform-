import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def train_model(data_path, model_path, vectorizer_path):
    df = pd.read_csv(data_path)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['description'])
    y = df['label']
    
    model = LogisticRegression()
    model.fit(X, y)
    
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    print("Training complete. Model and vectorizer saved.")

if __name__ == "__main__":
    train_model("data/raw/raw_claims_data.csv", "models/checkpoints/claims_classifier.joblib", "models/checkpoints/tfidf_vectorizer.joblib")
