from fastapi import APIRouter
from pydantic import BaseModel
from app.ml.inference import predict_roles
from app.utils.role_normalizer import normalize_role

router = APIRouter()

class JobRequest(BaseModel):
    job_description: str

@router.post("/")
def predict(data: JobRequest):
    results = predict_roles(data.job_description)

    top = results[0]
    top["role"] = normalize_role(top["role"])  # 🔥 FIX

    return {
        "top_match": top,
        "all_predictions": results[:5]
    }
