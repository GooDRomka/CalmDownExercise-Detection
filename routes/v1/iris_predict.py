from fastapi import APIRouter
import pandas as pd
from models.schemas.iris import Elomia, ElomiaPredictionResponse
import models.ml.classifier as clf
from models.ml.preproc import *
app_iris_predict_v1 = APIRouter()


@app_iris_predict_v1.post('/iris/predict',
                          tags=["Predictions"],
                          response_model=ElomiaPredictionResponse,
                          description="Get a classification from model")

async def get_prediction(data: Elomia):
    X_token = feature_create(pd.DataFrame.from_dict(data.data))
    prediction = clf.model.predict(X_token).tolist()
    print("model give prediction:\n\n", prediction)
    return {"prediction": prediction}

