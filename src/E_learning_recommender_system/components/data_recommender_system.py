import os
import sys
import joblib
import pandas as pd
from E_learning_recommender_system.logging import logging
from sklearn.metrics.pairwise import cosine_similarity
from E_learning_recommender_system.exception import CustomException
from E_learning_recommender_system.utils.common import preprocess_text
from E_learning_recommender_system.entity import DataRecommenderSystemConig

class DataRecommenderSystem:
    def __init__(self, config:DataRecommenderSystemConig):
        self.config = config

    def load_tfidf_vectorizer_and_transformed_data(self):
        try:
            self.tfidf_vectorizer = joblib.load(self.config.tf_idf_vectorizer)
            self.transformed_data = joblib.load(self.config.transformed_data)
        except Exception as e:
            return CustomException(e, sys)

    def recommend_courses(self, user_input):
        try:
            # Reading final.csv file
            data = pd.read_csv(self.config.final_data)
            # Preprocess the user input to make it compatible with the TF-IDF vectorizer
            user_input = preprocess_text(user_input)

            # Transform the preprocessed user input into a TF-IDF vector
            user_vector = self.tfidf_vectorizer.transform([user_input])

            # Compute the cosine similarity between the user's input and all courses in the TF-IDF matrix
            cosine_sim = cosine_similarity(user_vector, self.transformed_data)  # Use cosine_similarity

            # Create a list of tuples where each tuple contains the index of a course and its cosine similarity score
            sim_scores = list(enumerate(cosine_sim[0]))

            # Sort the list of course indices and cosine similarity scores in descending order based on the scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the top 5 similar courses (excluding the user's input itself)
            top_courses = sim_scores[1:6]

            # Extract the indices of the recommended courses from the sorted list
            course_indices = [i[0] for i in top_courses]

            # Retrieve the recommended courses from the original dataset using the course indices
            recommended_courses = data.iloc[course_indices]

            return recommended_courses
        except Exception as e:
            raise CustomException(e, sys)

    def display_recommendations(self, recommended_courses):
        try:
            for index, row in recommended_courses.iterrows():
                print("Course Name:", row['course_name'])
                print("Description:\n", row['description'])
                print("Learning Process:\n", row['learning'])
                print("Difficulty:", row['difficulty'])
                print("Rating:", row['Average rating'])
                print("Popularity:", row['Popularity'])
                print("-" * 100)
                print("\n")
        except Exception as e:
            raise CustomException(e, sys)
