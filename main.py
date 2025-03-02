from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.statge_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully!")
except Exception as e:
    logger.exception(e)
    raise e