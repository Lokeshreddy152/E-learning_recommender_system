import os
from E_learning_recommender_system.logging import logging
from E_learning_recommender_system.entity import DataValidationConig

class DataValidation:
    def __init__(self, config: DataValidationConig):
        self.config = config

    def validate_all_files_exist(self)->bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_transformation"))

            for file in all_files:
                if file not in self.config.all_required_files:
                    validation_status = False
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e
