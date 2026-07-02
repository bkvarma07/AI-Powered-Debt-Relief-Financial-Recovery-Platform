from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import SessionLocal
from models.user import User
from models.loan import Loan

from services.settlement_engine import calculate_settlement_prediction

router = APIRouter(
    prefix="/settlement",
    tags=["Settlement Prediction"]
)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/predict")
def settlement_prediction(db: Session = Depends(get_db)):
    """
    Settlement Prediction using database records.
    """

    # Get first user
    user = db.query(User).first()

    if not user:
        return {
            "message": "No user found in database."
        }

    # Get all loans of that user
    loans = db.query(Loan).filter(
        Loan.user_id == user.user_id
    ).all()

    if not loans:
        return {
            "message": "No loans found for this user."
        }

    # Calculate settlement prediction
    result = calculate_settlement_prediction(
        user,
        loans
    )

    return {
        "success": True,
        "user": user.name,
        "total_loans": len(loans),
        "settlement_prediction": result
    }