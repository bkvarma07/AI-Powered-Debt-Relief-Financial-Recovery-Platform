from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import SessionLocal
from models.user import User
from schemas.user import UserRegister, UserLogin, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered."
        }

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        monthly_income=user.monthly_income,
        monthly_expenses=user.monthly_expenses
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "success": True,
        "message": "User registered successfully.",
        "user_id": new_user.user_id
    }


@router.post("/login")
def login(user: UserLogin):
    return {
        "message": "Login API Working"
    }


@router.put("/update-profile")
def update_profile(user: UserUpdate):
    return {
        "message": "Profile Update API Working"
    }