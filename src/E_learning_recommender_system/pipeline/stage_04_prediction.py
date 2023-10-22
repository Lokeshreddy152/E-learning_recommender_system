import sys
from E_learning_recommender_system.config.configuration import  ConfigurationManger
from E_learning_recommender_system.components.data_recommender_system import DataRecommenderSystem
from E_learning_recommender_system.exception import CustomException


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManger.get_data_recommender_system_config
    
    def recommend_courses(self, user_input):
        data_recommender_system_config = self.config.get_data_recommender_system_config()
        data_recommender_system = DataRecommenderSystem(config=data_recommender_system_config)
        data_recommender_system.load_tfidf_vectorizer_and_transformed_data()

        recommended_courses = data_recommender_system.recommend_courses(user_input)

        if recommended_courses is not None:
            data_recommender_system.display_recommendations(recommended_courses)
        else:
            print("Recommendation process failed.")