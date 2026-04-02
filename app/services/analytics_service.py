from sqlalchemy.orm import Session
from app import models
from collections import defaultdict


def get_summary(db: Session):
    transactions = db.query(models.Transaction).all()

    income = sum(t.amount for t in transactions if t.type == "income")
    expense = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }


# CATEGORY BREAKDOWN
def get_category_breakdown(db: Session):
    transactions = db.query(models.Transaction).all()

    breakdown = defaultdict(float)

    for t in transactions:
        breakdown[t.category] += t.amount

    return dict(breakdown)


# RECENT TRANSACTIONS
def get_recent_transactions(db: Session, limit: int = 5):
    return (
        db.query(models.Transaction)
        .order_by(models.Transaction.date.desc())
        .limit(limit)
        .all()
    )