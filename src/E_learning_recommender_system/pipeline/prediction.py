import pandas as pd
import joblib
from E_learning_recommender_system.config.configuration import ConfigurationManger
from E_learning_recommender_system.utils.common import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity

class PredictionPipeline:
    def __init__(self):
        # Initialize the PredictionPipeline class.
        self.config = ConfigurationManger().get_data_transformation_config()  # Load configuration.

    def predict(self, text):
        # Method to make course recommendations based on user input.

        # Load the TF-IDF vectorizer and transformed data from the configuration.
        tf_idf_vectorizer = joblib.load(self.config.tf_idf_vectorizer)
        transformed_data = joblib.load(self.config.transformed_data)

        # Load the original course data from the configuration.
        data = pd.read_csv(self.config.final_data)

        # Preprocess the user input to make it compatible with the TF-IDF vectorizer.
        text = preprocess_text(text)

        # Transform the preprocessed user input into a TF-IDF vector.
        user_vector = tf_idf_vectorizer.transform([text])

        # Compute the cosine similarity between the user's input and all courses in the TF-IDF matrix.
        cosine_sim = cosine_similarity(user_vector, transformed_data)

        # Create a list of tuples where each tuple contains the index of a course and its cosine similarity score.
        sim_scores = list(enumerate(cosine_sim[0]))

        # Sort the list of course indices and cosine similarity scores in descending order based on the scores.
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the top 5 similar courses (excluding the user's input itself).
        top_courses = sim_scores[1:6]

        # Extract the indices of the recommended courses from the sorted list.
        course_indices = [i[0] for i in top_courses]

        # Retrieve the recommended courses from the original dataset using the course indices.
        recommended_courses = data.iloc[course_indices]

        # Create an empty list to store recommended courses.
        recommended_courses_list = []

        # Iterate through the recommended courses and create a dictionary for each course.
        for index, row in recommended_courses.iterrows():
            recommended_course = {
                "Course Name": row['course_name'],
                "Description": row['description'],
                "Learning Process": row['learning'],
                "Difficulty": row['difficulty'],
                "Rating": row['Average rating'],
                "Popularity": row['Popularity']
            }
            recommended_courses_list.append(recommended_course)

        # Return the list of recommended courses.
        return recommended_courses_list
