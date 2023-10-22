from E_learning_recommender_system.config.configuration import  ConfigurationManger
from E_learning_recommender_system.components.data_validation import DataValidation
from E_learning_recommender_system.logging import logging


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
       config = ConfigurationManger()
       data_validation_config = config.get_data_validation_config()
       data_validation = DataValidation(config=data_validation_config)
       data_validation.validate_all_files_exist()