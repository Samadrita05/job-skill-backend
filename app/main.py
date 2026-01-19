from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.auth import router as auth_router
from app.api.v1.predict import router as predict_router
from app.api.v1.skill_gap import router as skill_gap_router
from app.api.v1.roadmap import router as roadmap_router

app = FastAPI(title="AI Job & Skill Recommendation Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(predict_router, prefix="/api/v1/predict", tags=["Prediction"])
app.include_router(skill_gap_router, prefix="/api/v1/skill-gap", tags=["Skill Gap"])
app.include_router(roadmap_router, prefix="/api/v1/roadmap", tags=["Roadmap"])

@app.get("/")
def root():
    return {"message": "Backend is running"}
