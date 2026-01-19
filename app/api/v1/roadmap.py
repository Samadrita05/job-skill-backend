from fastapi import APIRouter
from app.data.career_roadmap import CAREER_ROADMAP
from app.utils.role_normalizer import normalize_role

router = APIRouter()

@router.get("/{role}")
def roadmap(role: str):
    role = normalize_role(role)
    return CAREER_ROADMAP.get(role, {})
