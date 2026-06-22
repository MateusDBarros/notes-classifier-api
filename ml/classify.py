"""
Loads the trained model once (at import time) and exposes a simple
classify(text) function for the rest of the app to use.

Loading once at import (not per-request) matters: joblib.load() reads
from disk and deserializes the pipeline, which is relatively slow.
Doing it once when the module is first imported means every request
afterward reuses the already-loaded model in memory.
"""

from .config import MODEL_PATH
import joblib

_model = None


def _get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


def classify(text: str) -> str:
    """Predicts a category tag for the given text. Returns one of:
    'work', 'personal', 'idea', 'urgent' (or whatever labels you trained on)."""
    model = _get_model()
    return model.predict([text])[0]
