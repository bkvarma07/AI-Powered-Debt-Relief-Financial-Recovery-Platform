from fastapi import APIRouter

from services.settlement_engine import calculate_settlement_prediction

router = APIRouter(
    prefix="/settlement",
    tags=["Settlement Prediction"]
)


@router.get("/predict")
def settlement_prediction():
    """
    Temporary demo endpoint.
    Story 4 will connect this with the database.
    """

    class DummyUser:
        monthly_income = 50000
        monthly_expenses = 20000

    class DummyLoan:
        def __init__(
            self,
            loan_id,
            lender_name,
            loan_type,
            outstanding_amount,
            interest_rate,
            emi,
            overdue_months
        ):
            self.loan_id = loan_id
            self.lender_name = lender_name
            self.loan_type = loan_type
            self.outstanding_amount = outstanding_amount
            self.interest_rate = interest_rate
            self.emi = emi
            self.overdue_months = overdue_months

    user = DummyUser()

    loans = [
        DummyLoan(
            1,
            "HDFC Bank",
            "Personal Loan",
            300000,
            14,
            12000,
            3
        ),
        DummyLoan(
            2,
            "SBI",
            "Education Loan",
            180000,
            9,
            6000,
            0
        )
    ]

    return calculate_settlement_prediction(user, loans)