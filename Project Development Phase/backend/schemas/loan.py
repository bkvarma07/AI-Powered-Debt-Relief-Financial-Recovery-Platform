from pydantic import BaseModel


class LoanCreate(BaseModel):
    loan_type: str
    loan_amount: float
    outstanding_amount: float
    interest_rate: float
    due_date: str