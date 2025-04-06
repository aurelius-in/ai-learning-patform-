from fastapi import APIRouter, HTTPException, status
from typing import List
from api.models.user import UserCreate, UserOut, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

fake_users_db = []

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate):
    new_user = {
        "id": len(fake_users_db) + 1,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": "hashed_" + user.password,
        "is_active": True,
        "is_admin": False,
        "created_at": "2025-01-01T00:00:00"
    }
    fake_users_db.append(new_user)
    return new_user

@router.get("/", response_model=List[UserOut])
async def list_users():
    return fake_users_db

@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserUpdate):
    for u in fake_users_db:
        if u["id"] == user_id:
            if user.full_name:
                u["full_name"] = user.full_name
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")