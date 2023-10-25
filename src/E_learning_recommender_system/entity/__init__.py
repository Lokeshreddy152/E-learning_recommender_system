from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    raw_data: str
    sql_query:str
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str

@dataclass(frozen=True)
class DataTransformationConig:
    root_dir: Path
    raw_data: str
    fet_eng_data: str
    text_preprocess_data: str
    final_data: str
    tf_idf_vectorizer: str 
    transformed_data: str 

@dataclass(frozen=True)
class DataValidationConig:
    root_dir: Path
    status_file: str
    all_required_files: list
