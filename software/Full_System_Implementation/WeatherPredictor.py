import joblib
from utils import extract_features_from_frame


svm_classifier = joblib.load('svm_classifier.joblib')


def predict_weather(frame, classifier):
    """Weather prediction for a given image frame"""
    features = extract_features_from_frame(frame)
    prediction = classifier.predict(features)
    return 'Sunny' if prediction == 1 else 'Not Sunny'
