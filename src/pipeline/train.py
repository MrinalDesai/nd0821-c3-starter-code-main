"""
Author: Mrinal Desai
Date: March, 2022
This script used to train and save the model
"""
import sys
import logging
from pipeline.model import get_model_pipeline, train_model


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def train(model, X_train, y_train, param_grid, feats):
    """
    trains pipeling




    """
    logging.info("Creating model pipeline")
    model_pipe = get_model_pipeline(model, feats)

    logging.info(f"Training {model.__class__.__name__} model")
    model_pipe = train_model(model_pipe, X_train, y_train, param_grid)

    return model_pipe
