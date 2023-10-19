from E_learning_recommender_system.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from E_learning_recommender_system.logging import logging


STAGE_NAME = "Data Ingestion stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(F">>>>>> stage {STAGE_NAME} completed<<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e