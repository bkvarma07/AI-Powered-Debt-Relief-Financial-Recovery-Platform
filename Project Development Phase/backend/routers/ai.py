from fastapi import APIRouter
from services.ai_engine import generate_negotiation_strategy

router = APIRouter(
    prefix="/ai",
    tags=["AI Negotiation"]
)


@router.get("/strategy")
def ai_strategy():

    class DummyUser:
        name = "Rahul Sharma"
        monthly_income = 50000
        monthly_expenses = 20000

    class DummyLoan:
        loan_id = 1
        lender_name = "HDFC Bank"
        loan_type = "Personal Loan"
        outstanding_amount = 300000
        interest_rate = 14
        emi = 12000
        overdue_months = 3

    return generate_negotiation_strategy(
        DummyUser(),
        DummyLoan()
    )