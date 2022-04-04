"""
Author: Mrinal Desai
Date: March, 2022
This script holds the config data for training model pipeline and running tests
related to the pipeline
"""
import os
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

TEST_SIZE = 0.3
RANDOM_STATE = 17
__MAIN_DIR = Path(__file__).parent.parent.absolute()

MODEL = RandomForestClassifier(
   class_weight='balanced',
   random_state=RANDOM_STATE)
# MODEL = LogisticRegression(
#     max_iter=2000,
#     class_weight='balanced',
#     random_state=RANDOM_STATE)

PARAM_GRID = None
if isinstance(MODEL, RandomForestClassifier):
    PARAM_GRID = {
        'model__n_estimators': list(range(50, 151, 25)),
        'model__max_depth': list(range(2, 11, 2)),
        'model__min_samples_leaf': list(range(1, 51, 5)),
    }
elif isinstance(MODEL, LogisticRegression):
    PARAM_GRID = {
        'model__C': np.linspace(0.1, 10, 3)
    }

FEATURES = {
    'categorical': [
        'marital_status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'workclass',
        'native_country'


    ],
    'numeric': [
        'age',
        'fnlgt',
        'capital_gain',
        'capital_loss',
        'hours_per_week'

    ],
    'drop': [
        'education'


    ]
}

SLICE_COLUMNS = ['sex', 'race']
################################################################
__DATA_FILE = 'edited_census.csv'
#__DATA_FILE_SR= 'edited_census_salary_removed.csv'
__MODEL_FILE = 'pipe_' + MODEL.__class__.__name__
__EVAL_FILE = f'model_evaluation_{MODEL.__class__.__name__}.txt'
################################################################
__SLICE_FILE = f'output_slice_op_{MODEL.__class__.__name__}.txt'
__ENCODER_FILE = f'pipe_encoder_{ MODEL.__class__.__name__}.joblib'

DATA_DIR = os.path.join(__MAIN_DIR, 'data', __DATA_FILE)
#DATA_DIR_SR = os.path.join(__MAIN_DIR, 'data', __DATA_FILE_SR)
MODEL_DIR = os.path.join(__MAIN_DIR, 'models', __MODEL_FILE)
ENCODER_DIR = os.path.join(__MAIN_DIR, 'models', __ENCODER_FILE)
################################################################
EVAL_DIR = os.path.join(__MAIN_DIR, 'model_metrics', __EVAL_FILE)
SLICE_DIR = os.path.join(__MAIN_DIR, 'model_metrics', __SLICE_FILE)
################################################################
PLOT_DIR = os.path.join(__MAIN_DIR, 'diagrams')
EXAMPLES_DIR = os.path.join(__MAIN_DIR, 'src', 'app', 'examples.yaml')
