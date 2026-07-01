from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.connection import Base


class Loan(Base):
    __tablename__ = "loans"

    loan_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    loan_type = Column(String, nullable=False)
    loan_amount = Column(Float, nullable=False)
    outstanding_amount = Column(Float, nullable=False)
    interest_rate = Column(Float)
    due_date = Column(String)