from E_learning_recommender_system.constants import CONFIG_FILE_PATH
from E_learning_recommender_system.utils.common import read_yaml,create_directories
from E_learning_recommender_system.entity import (DataIngestionConfig,
                                                  DataTransformationConig,
                                                  DataValidationConig,
                                                  DataRecommenderSystemConig)


class ConfigurationManger:
    def __init__(self,config_filepath = CONFIG_FILE_PATH):

        self.config = read_yaml(config_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            raw_data= config.raw_data,
            sql_query= config.sql_query,
            db_host = config.db_host,
            db_port = config.db_port ,   
            db_name = config.db_name,
            db_user = config.db_user,
            db_password = config.db_password
        )       

        return data_ingestion_config
    
    def get_data_transformation_config(self)->DataTransformationConig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConig(
            root_dir=config.root_dir,
            raw_data=config.raw_data,
            fet_eng_data = config.fet_eng_data,
            text_preprocess_data = config.text_preprocess_data,
            final_data = config.final_data,
            tf_idf_vectorizer  = config.tf_idf_vectorizer,
            transformed_data = config.transformed_data
        )       
        
        return data_transformation_config
    
    def get_data_validation_config(self)->DataValidationConig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            all_required_files=config.all_required_files
        )       

        return data_validation_config
    def get_data_recommender_system_config(self)->DataRecommenderSystemConig:
        config = self.config.data_recommender_system

        data_recommender_system_config = DataRecommenderSystemConig(
            final_data=config.final_data,
            tf_idf_vectorizer= config.tf_idf_vectorizer,
            transformed_data= config.transformed_data
        )       

        return data_recommender_system_config