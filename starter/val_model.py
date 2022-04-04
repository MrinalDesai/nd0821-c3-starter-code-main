



from joblib import load
from .ml.model import compute_score_per_slice

##############################################################3333333
def val_model(test_df, cat_features, root_dir):

    # load model and encoder
    trained_model = load(f"{root_dir}/model/model.joblib")
    encoder = load(f"{root_dir}/model/encoder.joblib")
    lb = load(f"{root_dir}/model/lb.joblib")

    compute_score_per_slice(
        trained_model,
        test_df,
        encoder,
        lb,
        cat_features,
        root_dir)
