import os
import pandas as pd
import psycopg2
from E_learning_recommender_system.logging import logging
from E_learning_recommender_system.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def extracted_data_from_sql(self):
        if not os.path.exists(self.config.raw_data):
            # Establish a connection to the PostgreSQL database
            connection = psycopg2.connect(
                host=self.config.db_host,
                port=self.config.db_port,
                database=self.config.db_name,
                user=self.config.db_user,
                password=self.config.db_password
            )

            try:
                # Execute the SQL query and fetch data into a Pandas DataFrame
                data = pd.read_sql_query(self.config.sql_query, connection)
                
                # Define the path to save the extracted data as a CSV file
                output_path = self.config.raw_data

                # Save the data to a CSV file
                data.to_csv(output_path, index=False)

                logging.info(f"Data extracted and saved to {output_path}")
            finally:
                # Close the database connection, regardless of success or failure
                connection.close()
        else:
            logging.info(f"CSV file already exists at {self.config.raw_data}")