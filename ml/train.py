"""
Trains a small text classifier on the labeled notes and saves it to disk.

Pipeline: TfidfVectorizer (text -> numeric features) + LogisticRegression
(numeric features -> category prediction).

Why TF-IDF + LogisticRegression for this:
- Dataset is tiny (~20-30 examples) -> deep learning would overfit badly
- Text is short and category-specific words matter a lot ("urgent", "fix",
  "gym", "idea") -> TF-IDF captures "which words matter" well
- LogisticRegression is fast, interpretable, and a sane default for small
  text classification before reaching for anything fancier

Run with:
    python -m ml.train
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from .training_data import TRAINING_DATA
from sklearn.pipeline import Pipeline
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "note_classifier.joblib")

texts, labels = zip(*TRAINING_DATA)

print(texts)
print(labels)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', LogisticRegression())])

pipeline.fit(texts, labels)
joblib.dump(pipeline, MODEL_PATH)
print(f'Model save here {MODEL_PATH}')
