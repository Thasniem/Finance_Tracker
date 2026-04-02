from sqlalchemy.orm import Session
from app import models


# ================= USERS =================

def create_user(db: Session, user):
    """Create a new user"""
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    """Get all users"""
    return db.query(models.User).all()


# ================= TRANSACTIONS =================

def create_transaction(db: Session, transaction, user_id: int):
    """Create a transaction linked to a user"""
    db_txn = models.Transaction(**transaction.dict(), user_id=user_id)
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn


def get_transactions(db: Session, type=None, category=None, start_date=None, end_date=None):
    """Fetch transactions with optional filters"""
    query = db.query(models.Transaction)

    if type:
        query = query.filter(models.Transaction.type == type)
    if category:
        query = query.filter(models.Transaction.category == category)
    if start_date:
        query = query.filter(models.Transaction.date >= start_date)
    if end_date:
        query = query.filter(models.Transaction.date <= end_date)

    return query.all()


def update_transaction(db: Session, txn_id: int, txn_data):
    """Update a transaction"""
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()

    if not txn:
        return None

    for key, value in txn_data.dict(exclude_unset=True).items():
        setattr(txn, key, value)

    db.commit()
    db.refresh(txn)
    return txn


def delete_transaction(db: Session, txn_id: int):
    """Delete a transaction"""
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()

    if not txn:
        return None

    db.delete(txn)
    db.commit()
    return txn