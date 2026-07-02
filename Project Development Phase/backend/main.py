from fastapi import FastAPI

from database.connection import Base, engine

# Import all models
from models.user import User
from models.loan import Loan
from models.financial_profile import FinancialProfile
from models.settlement import SettlementRecord
from models.ai_history import AIHistory

# Import routers
from routers.users import router as user_router
from routers.settlement import router as settlement_router
from routers.ai import router as ai_router

app = FastAPI(
    title="FinRelief AI",
    version="0.1.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(user_router)
app.include_router(settlement_router)
app.include_router(ai_router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to FinRelief AI 🚀",
        "status": "running"
    }