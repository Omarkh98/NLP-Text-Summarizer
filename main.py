from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.statge_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully!")
except Exception as e:
    logger.exception(e)
    raise e