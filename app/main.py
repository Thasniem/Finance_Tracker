from fastapi import FastAPI
from app.routes import transactions, users, analytics
from app.database import Base, engine
from app.config import settings

# ✅ IMPORTANT: import models BEFORE create_all
from app import models

# Create DB tables
Base.metadata.create_all(bind=engine)

# App instance
app = FastAPI(title=settings.app_name)

# Routers
app.include_router(users.router)
app.include_router(transactions.router)
app.include_router(analytics.router)