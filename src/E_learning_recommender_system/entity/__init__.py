from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    extract_data: Path
    raw_data: str
    sql_query:str
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_password: str