from dataclasses import dataclass
import os
import sys
from catboost import CatBoostRegressor
from xgboost import XGBRegressor

from src.utils import evaluate_models,save_object
from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor

@dataclass
class ModelTrainerConfig:

    def __init__(self):

        self.model_path=os.path.join("artifacts","model.pkl")


class ModelTrainer:
        def __init__(self):
             self.model_trainer=ModelTrainerConfig()

        def initiate_model_trainer(self,train_arr,test_arr):
             
             try:
                  logging.info('Splitting training and testing')

                  x_train,y_train,x_test,y_test=(
                       train_arr[:,:-1],
                       train_arr[:,-1],
                       test_arr[:,:-1],
                       test_arr[:,-1]

                  )
                  params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }
                  
                  models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
                  
                  
                  model_report:dict=evaluate_models(X_train=x_train,y_train=y_train,X_test=x_test,y_test=y_test,
                                             models=models,param=params)
                  

                  maximum=max(sorted(model_report.values()))


                  best_model_name=list(model_report.keys())[
                       list(model_report.values()).index(maximum)
                  ]

                  best_model=models[best_model_name]


                  if    maximum<0.6:
                       raise CustomException("No best model found")
                  

                  logging.info("best model found")


                  save_object(
                       file_path=self.model_trainer.model_path,
                       obj=best_model
                                                           )
                  
                  prediction=  best_model.predict(x_test)
                  

                  r2_square=r2_score(y_test,   prediction)

                  return r2_square



             except Exception as e:
                  raise CustomException(e,sys)
                  
             
             
