from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import SessionLocal
from models.loan import Loan
from schemas.loan import LoanCreate

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add")
def add_loan(
    user_id: int,
    loan: LoanCreate,
    db: Session = Depends(get_db)
):

    new_loan = Loan(
        user_id=user_id,
        loan_type=loan.loan_type,
        loan_amount=loan.loan_amount,
        outstanding_amount=loan.outstanding_amount,
        interest_rate=loan.interest_rate,
        due_date=loan.due_date,
        lender_name=loan.lender_name,
        emi=loan.emi,
        overdue_months=loan.overdue_months
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return {
        "success": True,
        "message": "Loan added successfully.",
        "loan_id": new_loan.loan_id
    }


@router.get("/user/{user_id}")
def get_user_loans(
    user_id: int,
    db: Session = Depends(get_db)
):

    loans = db.query(Loan).filter(
        Loan.user_id == user_id
    ).all()

    return {
        "success": True,
        "total_loans": len(loans),
        "loans": loans
    }


@router.delete("/{loan_id}")
def delete_loan(
    loan_id: int,
    db: Session = Depends(get_db)
):
    loan = db.query(Loan).filter(Loan.loan_id == loan_id).first()
    if not loan:
        return {
            "success": False,
            "message": "Loan not found."
        }
    
    db.delete(loan)
    db.commit()
    
    return {
        "success": True,
        "message": "Loan deleted successfully."
    }