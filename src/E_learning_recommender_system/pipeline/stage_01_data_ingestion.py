from E_learning_recommender_system.config.configuration import  ConfigurationManger
from E_learning_recommender_system.components.data_ingestion import DataIngestion
from E_learning_recommender_system.logging import logging

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extracted_data_from_sql()