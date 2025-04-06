from src.models.predict import predict

def run_inference_pipeline():
    sample_text = "Routine dental cleaning and x-ray"
    model_path = "models/checkpoints/claims_classifier.joblib"
    vectorizer_path = "models/checkpoints/tfidf_vectorizer.joblib"

    print("Running inference pipeline...")
    prediction = predict(sample_text, model_path, vectorizer_path)
    print("Prediction result:", prediction)

if __name__ == "__main__":
    run_inference_pipeline()
