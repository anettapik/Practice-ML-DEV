from enum import Enum


class AvailableModels(str, Enum):
    logreg_tfidf = "logreg_tfidf"
    catboost = "catboost"
    svm = "svm"