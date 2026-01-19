from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    # ✅ Dummy login for project
    if data.email == "admin@test.com" and data.password == "admin123":
        return {
            "access_token": "dummy-token",
            "token_type": "bearer"
        }

    raise HTTPException(status_code=401, detail="Invalid email or password")
