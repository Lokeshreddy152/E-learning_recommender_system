from E_learning_recommender_system.constants import CONFIG_FILE_PATH
from E_learning_recommender_system.utils.common import read_yaml,create_directories
from E_learning_recommender_system.entity import DataIngestionConfig

class ConfigurationManger:
    def __init__(self,config_filepath = CONFIG_FILE_PATH):

        self.config = read_yaml(config_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        create_directories([config.extract_data])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            extract_data= config.extract_data,
            raw_data= config.raw_data,
            sql_query= config.sql_query,
            db_host = config.db_host,
            db_port = config.db_port ,   
            db_name = config.db_name,
            db_user = config.db_user,
            db_password = config.db_password
        )       

        return data_ingestion_config