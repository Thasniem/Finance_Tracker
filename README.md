# 💰FINANCE TRACKER API PROJECT


## Project Overview

This project is a Python-based backend finance tracking system built using FastAPI. It allows users to manage financial transactions, apply filters, and generate useful financial insights. The system is designed with clean architecture, validation, and role-based access control.


## Project Structure

```
Finance_Tracker/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   ├── routes/
│   │   ├── transactions.py
│   │   ├── users.py
│   │   └── analytics.py
│   │
│   ├── services/
│   │   └── analytics_service.py
│   │
│   ├── utils/
│   │   └── role_checker.py
│   │
│   └── config.py
│
├── requirements.txt
└── README.md

```


## Objectives

-   Build a structured backend system using Python
-   Implement CRUD operations
-   Provide analytics and summaries
-   Apply role-based access control
-   Ensure validation and error handling


## Tech Stack

-   Python
-   FastAPI
-   SQLAlchemy
-   SQLite
-   Pydantic


## Setup Instructions

1. **Clone the repository:**

```bash
git clone <https://github.com/Thasniem/Finance_Tracker>
cd Finance_Tracker
```

2. **Create virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the root directory**

```env
DATABASE_URL=sqlite:///./finance.db
```

5. **Run the server:**

```bash
uvicorn app.main:app --reload
```


## User Roles

- Admin: Full access (Create, Update, Delete)
- Analyst: Create and view transactions (Cannot update/delete)
- Viewer: View-only access (Read-only)


## Transaction Details

Each transaction includes: 
- Amount
- Type (Income / Expense)
- Category
- Date
- Notes


## Features
- CRUD operations for transactions
- Filtering by category, type, and date
- Financial analytics
- Role-based access control
- Input validation and error handling


## Validation & Error Handling

-   Rejects negative amounts
-   Restricts invalid transaction types
-   Handles missing/incorrect input


## Database Design

-   SQLite database
-   One-to-Many: One User → Many Transactions


## API Usage

The API can be tested using Swagger UI or Postman.

**Users**
- POST /users/

**Transactions**
- POST /transactions/
- GET /transactions/
- PUT /transactions/{txn_id}
- DELETE /transactions/{txn_id}

**Analytics**
- GET /analytics/summary
- GET /analytics/category-breakdown
- GET /analytics/recent

**Role-Based Access**
Include role in request headers:
- X-Role: admin
- X-Role: analyst
- X-Role: viewer


## API Documentation

Interactive API documentation is available via Swagger UI:

<http://127.0.0.1:8000/docs>


## Response Codes

| Code | Meaning |
|------|--------|
| 200 | Success |
| 422 | Validation Error |
| 403 | Unauthorized |
| 404 | Not Found |


## Assumptions

- User roles are passed via request headers (X-Role) instead of implementing full authentication
- SQLite is used as the database for simplicity and easy setup
- Each transaction is linked to a user using user_id
- Basic role-based access is implemented without advanced security mechanisms
- The system is designed for demonstration purposes and not for production use


## Testing
Tested using Swagger and Postman


## Conclusion

This project demonstrates a clean and structured backend system with proper API design, validation, and role-based access control. It reflects strong understanding of Python backend development, database handling, and real-world application logic.