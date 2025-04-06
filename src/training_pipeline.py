from src.models.train import train_model

def run_training_pipeline():
    data_path = "data/raw/raw_claims_data.csv"
    model_path = "models/checkpoints/claims_classifier.joblib"
    vectorizer_path = "models/checkpoints/tfidf_vectorizer.joblib"

    print("Starting training pipeline...")
    train_model(data_path, model_path, vectorizer_path)
    print("Training pipeline completed.")

if __name__ == "__main__":
    run_training_pipeline()