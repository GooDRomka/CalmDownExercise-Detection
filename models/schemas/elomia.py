from pydantic import BaseModel, conlist
from typing import Any, Dict, List


class Elomia(BaseModel):
    data: Dict[str, List[str]]


class ElomiaPredictionResponse(BaseModel):
    prediction: List[int]
