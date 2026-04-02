from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.analytics_service import (
    get_summary,
    get_category_breakdown,
    get_recent_transactions
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    """
    Get overall financial summary including total income, expenses, and balance.
    """
    return get_summary(db)


# CATEGORY ANALYTICS
@router.get("/category-breakdown")
def category_breakdown(db: Session = Depends(get_db)):
    """
    Get category-wise breakdown of all transactions.
    """
    return get_category_breakdown(db)


# RECENT TRANSACTIONS
@router.get("/recent")
def recent_transactions(db: Session = Depends(get_db)):
    """
    Get the most recent transactions (latest first).
    """
    return get_recent_transactions(db)