import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.svm import LinearSVR
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiat_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (train_array[:, :-1], train_array[:,-1],
                                                test_array[:,:-1], train_array[:,-1])
            models = {
                "LinearRegressor": LinearRegression(),
                "LassoRegressor": Lasso(),
                "RidgeRegressor": Ridge(),
                "SVRegressor": LinearSVR(),
                "DecisionRegressor": DecisionTreeRegressor(),
                "RandomForestRegressor": RandomForestRegressor(),
                "AdaboostRegressor": AdaBoostRegressor(),
                "XgboostRegressor": XGBRegressor(),
                "CatboostRegressor": CatBoostRegressor(),
            }


        except:
            pass