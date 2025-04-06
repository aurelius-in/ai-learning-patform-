import numpy as np
import pickle

# Load similarity matrix
with open("similarity_matrix.pkl", "rb") as f:
    similarity_matrix = pickle.load(f)

# Mock course list
courses = ["Smart Document Bot", "Claims Triage AI", "MindTrace", "Neurodegenerative Detection"]

def recommend(course_index, top_n=2):
    similarities = similarity_matrix[course_index]
    recommended_indices = similarities.argsort()[-top_n-1:-1][::-1]
    return [courses[i] for i in recommended_indices]

if __name__ == "__main__":
    course_id = 0  # Smart Document Bot
    recommendations = recommend(course_id)
    print(f"Recommended courses for '{courses[course_id]}': {recommendations}")
