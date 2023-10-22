import pandas as pd
import joblib
import os
from E_learning_recommender_system.logging import logging
from E_learning_recommender_system.utils.common import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
from E_learning_recommender_system.entity import DataTransformationConig


class DataTransformation:
    def __init__(self, config: DataTransformationConig):
        self.config = config
        
    def feature_engineering(self):
        if not os.path.exists(self.config.fet_eng_data):
            logging.info(f">>>>> Feture Engneering is started <<<<<<")

            df = pd.read_csv(self.config.raw_data)
            # Calculate average rating for each course
            average_rating = df.groupby('course_id')['rating'].mean().reset_index()
            average_rating.rename(columns={'rating': 'Average rating'}, inplace=True)
            average_rating['Average rating'] = average_rating['Average rating'].round(1)

            # Calculate number of reviews for each course
            num_reviews = df.groupby('course_id')['rating'].count().reset_index()
            num_reviews.rename(columns={'rating': 'Number of reviews'}, inplace=True)

            # Calculate popularity based on the number of reviews
            popularity = num_reviews.copy()
            popularity['Popularity'] = pd.qcut(popularity['Number of reviews'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])

            # Select the desired columns from the original DataFrame
            selected_columns = ['course_id', 'course_name', 'difficulty', 'description', 'learning', 'tags']
            df_selected = df[selected_columns].drop_duplicates()

            # Merge the calculated metrics with the selected columns
            result_df = df_selected.merge(average_rating, on='course_id', how='left')
            result_df = result_df.merge(num_reviews, on='course_id', how='left')
            result_df = result_df.merge(popularity[['course_id', 'Popularity']], on='course_id', how='left')

            # Saving feture Engineering Data

            result_df.to_csv(self.config.fet_eng_data,index=False)

            logging.info(f">>>>>> Feture Engneering is completed and saved in {self.config.fet_eng_data}")

    def text_preprocessing(self):
        if not os.path.exists(self.config.text_preprocess_data):
            logging.info(">>>>> Text Preprocessing is started <<<<<<")
            # Reading fet_eng_files
            df_new = pd.read_csv(self.config.fet_eng_data)
            # Apply text preprocessing to your columns
            df_new['tags_preprocessed'] = df_new['tags'].apply(preprocess_text)
            df_new['description_preprocessed'] = df_new['description'].apply(preprocess_text)
            df_new['course_name_preprocessed'] = df_new['course_name'].apply(preprocess_text)

            # Optionally, you can combine the preprocessed columns into a single column
            df_new['combined_text'] = df_new['tags_preprocessed'] + ' ' + df_new['description_preprocessed'] + ' ' + df_new['course_name_preprocessed']

            # If you want to drop the preprocessed columns, you can use the following code:
            df_new.drop(['tags_preprocessed', 'description_preprocessed', 'course_name_preprocessed'], axis=1, inplace=True)

            # Save the preprocessed dataset if needed
            df_new.to_csv(self.config.text_preprocess_data, index=False)

            logging.info(f">>>>>> Text Preprocessing is Completed and saved in {self.config.text_preprocess_data}")

    def word_embedding(self):
        if not os.path.exists(self.config.transformed_data):
            logging.info(">>>>>>Word Embending is started with tf-idf Vectorizer<<<<<<")

            #Reading Text_preprocess_data
            df = pd.read_csv(self.config.text_preprocess_data)

            tfidf_vectorizer = TfidfVectorizer()
            tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_text'])

            # Save the TfidfVectorizer to disk
            joblib.dump(tfidf_vectorizer, self.config.tf_idf_vectorizer)

            # Save the transformed data to disk
            joblib.dump(tfidf_matrix, self.config.transformed_data)

            logging.info(f"TF-IDF vectorizer and matrix  as saved to {self.config.tf_idf_vectorizer}and{self.config.transformed_data}")
        else:
            logging.info(f"TF-IDF matrix already exists at {self.config.transformed_data}")

    def final_data(self):
        if not os.path.exists(self.config.final_data):
            logging.info(">>>>>>Removing Un-necessary features<<<<<<")
            df = pd.read_csv(self.config.fet_eng_data)

            # Adding required features only
            req_features = ['course_name','description','learning','difficulty','Average rating','Popularity']
            final = df[req_features]

            final.to_csv(self.config.final_data,index=False)

            logging.info(">>>>>>final data-set as saved<<<<<<")    