import models.ml.classifier as clf
from fastapi import FastAPI
from joblib import load
from routes.v1.elomia_predict import app_elomia_predict_v1
from routes.home import app_home


app = FastAPI(title="CalmDownExercise Detection", description="API for Elomia ml model", version="1.0")


@app.on_event('startup')
async def load_model():
    clf.model = load('models/ml/model_GB_with_fr.mdl')


app.include_router(app_home)
app.include_router(app_elomia_predict_v1, prefix='/v1')

