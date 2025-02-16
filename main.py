from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully!")
except Exception as e:
    logger.exception(e)
    raise e