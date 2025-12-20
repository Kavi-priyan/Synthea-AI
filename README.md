# Synthéa-AI
# A Student Performance Prediction - ML Pipeline

An end-to-end machine learning pipeline that predicts student math scores based on demographic factors and test performance. Built with Flask, scikit-learn, and deployed on Render for production use.

## Features

- **Complete ML Pipeline**: Automated data ingestion, transformation, and model training
- **Multiple Regression Models**: Implements Random Forest, XGBoost, CatBoost, Gradient Boosting, and more
- **Hyperparameter Tuning**: GridSearchCV for optimal model selection
- **Production-Ready Deployment**: Flask API deployed on Render with Gunicorn
- **Data Preprocessing**: Advanced ColumnTransformer pipeline with StandardScaler and OneHotEncoder
- **Interactive Web Interface**: HTML forms for real-time predictions
- **Model Persistence**: Serialized models using Joblib/Dill for efficient loading

## Tech Stack

- Python 3.11
- Flask 3.0.0 (Web Framework)
- scikit-learn 1.6.0 (ML Models)
- pandas 2.2.3 (Data Processing)
- NumPy 2.2.0 (Numerical Computing)
- XGBoost, CatBoost (Gradient Boosting)
- Gunicorn (WSGI Server)
- Render (Cloud Deployment)

## Model Performance

The pipeline evaluates 7 regression algorithms and automatically selects the best performer based on R² score, achieving production-grade accuracy for student performance prediction.

## Use Cases

- Educational institutions predicting student outcomes
- Early intervention systems for at-risk students
- Academic performance analysis and research
- Machine learning education and portfolio projects

## Keywords

`machine-learning` `flask` `scikit-learn` `student-performance` `regression` `xgboost` `catboost` `ml-pipeline` `data-science` `python` `deployment` `render` `predictive-analytics` `education-technology` `gradient-boosting`
