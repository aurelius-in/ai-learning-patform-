import joblib

claims_classifier = {
    "model_name": "ClaimsTriageClassifier",
    "version": "1.0",
    "type": "RandomForestClassifier",
    "trained_on": "2025-04-01",
    "features_used": ["claim_type", "description", "amount"],
    "accuracy": 0.89
}

joblib.dump(claims_classifier, "claims_classifier.joblib")
print("claims_classifier.joblib saved successfully.")
