

from cnnClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_2_preparation_base_model import PrepareBaseModelPipeline
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"
### Data Ingestion Phase ####


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Praparation of base model stage"
### Data Ingestion Phase ####
   
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e