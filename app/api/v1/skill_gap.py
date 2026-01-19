from fastapi import APIRouter
from app.data.role_skills import ROLE_SKILLS
from app.utils.role_normalizer import normalize_role
import re

router = APIRouter()

def normalize_skill(skill: str) -> str:
    """
    Normalize skill text:
    - lowercase
    - remove special characters
    - collapse spaces
    """
    skill = skill.lower()
    skill = re.sub(r"[^a-z0-9\s]", " ", skill)
    skill = re.sub(r"\s+", " ", skill).strip()
    return skill

@router.post("/")
def skill_gap(payload: dict):
    raw_role = payload.get("role", "")
    description = payload.get("description", "")

    role = normalize_role(raw_role)

    required_skills = ROLE_SKILLS.get(role, [])

    # Normalize job description once
    normalized_description = normalize_skill(description)

    present_skills = []
    missing_skills = []

    for skill in required_skills:
        normalized_skill = normalize_skill(skill)

        if normalized_skill in normalized_description:
            present_skills.append(skill)
        else:
            missing_skills.append(skill)

    return {
        "role_used": role,
        "required_skills": required_skills,
        "present_skills": present_skills,
        "recommended_skills": missing_skills
    }
