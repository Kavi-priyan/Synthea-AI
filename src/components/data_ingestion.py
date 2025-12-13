import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_join:str=os.path.join('artifacts','train.csv')
    test_data_join:str=os.path.join('artifacts','test.csv')
    raw_data_join:str=os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()