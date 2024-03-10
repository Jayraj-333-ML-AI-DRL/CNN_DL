

from cnnClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_2_preparation_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_3_model_traning import TrainingModelPipeline
from cnnClassifier.pipeline.stage_4_data_validation import Evaluationpipline
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.components.Training_model import  Training
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
    
    
    
    STAGE_NAME = "Model Training stage"
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model evaluation stage"





if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = Evaluationpipline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e   
