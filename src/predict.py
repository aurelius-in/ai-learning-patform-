import joblib

def predict(text, model_path, vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    X = vectorizer.transform([text])
    return model.predict(X)[0]

if __name__ == "__main__":
    label = predict("Emergency room visit for chest pain", "models/checkpoints/claims_classifier.joblib", "models/checkpoints/tfidf_vectorizer.joblib")
    print("Predicted label:", label)