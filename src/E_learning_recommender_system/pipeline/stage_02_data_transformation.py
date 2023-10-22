from E_learning_recommender_system.config.configuration import  ConfigurationManger
from E_learning_recommender_system.components.data_transformation import DataTransformation
from E_learning_recommender_system.logging import logging


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.feature_engineering()
        data_transformation.text_preprocessing()
        data_transformation.word_embedding()
        data_transformation.final_data()