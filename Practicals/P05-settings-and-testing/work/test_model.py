import numpy as np
import yaml

from pathlib import Path
from delivery.data import load_orders, split_orders
from delivery.model import train_model

WORK = Path(__file__).resolve().parent
P05_DIR = WORK.parent


def test_model_predictions_are_finite_and_positive():
    config = yaml.safe_load((WORK / "config.yaml").read_text(encoding="utf-8"))
    df = load_orders(P05_DIR / config["data"]["path"])
    X_train, X_test, y_train, y_test = split_orders(
        df, test_size=config["split"]["test_size"]
    )
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    assert len(predictions) == len(X_test)
    assert np.isfinite(predictions).all()
    assert (predictions > 0).all()
