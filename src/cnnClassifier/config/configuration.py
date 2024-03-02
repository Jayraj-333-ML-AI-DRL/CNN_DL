

from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.confiug_entity import DataIngestionConfig



class ConfigurationManager:
    def __init__(self, 
                 config_path = CONFIG_PATH,
                 params_path =PARAMS_PATH
                 
                 ):
                 
        self.config = read_yaml(CONFIG_PATH)
        self.params = read_yaml(PARAMS_PATH)
        
        
        create_directories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            
            create_directories([config.root_dir])
            
            data_ingestin_config = DataIngestionConfig(
                root_dir=config.root_dir,
    
                source_URL=config.source_URL,
                local_data_file= config.local_data_file,
                unzip_dir=config.unzip_dir
                
                
                         )   
            
            return data_ingestin_config