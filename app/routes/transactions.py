from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.database import get_db
from app import schemas, crud
from app.utils.role_checker import (
    get_role,
    require_admin,
    require_analyst_or_admin,
    require_any_role
)

router = APIRouter(prefix="/transactions", tags=["Transactions"])


# ================= CREATE =================
@router.post("/", response_model=schemas.TransactionResponse)
def create_transaction(
    txn: schemas.TransactionCreate,
    user_id: int = Query(..., description="User ID for the transaction"),
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    """
    Create a new transaction for a user.
    Accessible by Admin and Analyst roles.
    """
    require_analyst_or_admin(role)
    return crud.create_transaction(db, txn, user_id)


# ================= GET (FILTERED) =================
@router.get("/", response_model=list[schemas.TransactionResponse])
def get_transactions(
    type: str | None = Query(None, description="Transaction type (income/expense)"),
    category: str | None = Query(None, description="Transaction category"),
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    """
    Fetch transactions with optional filters:
    - type
    - category
    - date range
    Accessible by all roles.
    """
    require_any_role(role)
    return crud.get_transactions(db, type, category, start_date, end_date)


# ================= UPDATE =================
@router.put("/{txn_id}", response_model=schemas.TransactionResponse)
def update_transaction(
    txn_id: int,
    txn: schemas.TransactionUpdate,
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    """
    Update an existing transaction.
    Accessible only by Admin.
    """
    require_admin(role)

    updated = crud.update_transaction(db, txn_id, txn)
    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return updated


# ================= DELETE =================
@router.delete("/{txn_id}")
def delete_transaction(
    txn_id: int,
    role: str = Depends(get_role),
    db: Session = Depends(get_db)
):
    """
    Delete a transaction by ID.
    Accessible only by Admin.
    """
    require_admin(role)

    deleted = crud.delete_transaction(db, txn_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Deleted successfully"}