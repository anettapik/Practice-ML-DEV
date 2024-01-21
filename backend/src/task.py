import catboost
import pickle
import pandas as pd

from src.database.session_manager import get_session_maker
from src.repository.predictions import PredictionRepository


async def save_prediction(results: list[int], prediction_ids: list[int]) -> None:
    session_maker = await get_session_maker()
    async with session_maker() as session:
        await PredictionRepository.update_prediction(prediction_ids, results, session)


svm_model = pickle.load("models/svm_model.joblib")
logreg_model = pickle.load("models/logreg_tfidf.joblib")
catboost_model = catboost.CatBoostClassifier().load_model("models/catboost.model")

async def svm_model_predict(data: pd.DataFrame, prediction_ids: list[int]) -> None:
    predictions = svm_model.predict(data)
    await save_prediction(predictions, prediction_ids)


async def logreg_model_predict(data: pd.DataFrame, prediction_ids: list[int]) -> None:
    predictions = logreg_model.predict(data)
    await save_prediction(predictions, prediction_ids)


async def catboost_model_predict(data: pd.DataFrame, prediction_ids: list[int]) -> None:
    predictions = catboost_model.predict(data)
    await save_prediction(predictions, prediction_ids)
