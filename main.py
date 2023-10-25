from E_learning_recommender_system.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from E_learning_recommender_system.pipeline.stage_02_data_transformation import DataTransformationPipeline
from E_learning_recommender_system.pipeline.stage_03_data_validation import DataValidationPipeline
from E_learning_recommender_system.logging import logging
from E_learning_recommender_system.pipeline.prediction import PredictionPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(F">>>>>> stage {STAGE_NAME} completed<<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logging.info(F">>>>>> stage {STAGE_NAME} completed<<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataValidationPipeline()
    data_transformation.main()
    logging.info(F">>>>>> stage {STAGE_NAME} completed<<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e
