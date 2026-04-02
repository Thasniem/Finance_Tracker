from fastapi import Header, HTTPException

# Extract role from request header
def get_role(x_role: str = Header(...)):
    return x_role.lower()


# Only admin allowed
def require_admin(role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")


# Admin + Analyst allowed
def require_analyst_or_admin(role: str):
    if role not in ["admin", "analyst"]:
        raise HTTPException(status_code=403, detail="Access denied")


# Viewer, Analyst, Admin allowed (for read-only)
def require_any_role(role: str):
    if role not in ["admin", "analyst", "viewer"]:
        raise HTTPException(status_code=403, detail="Invalid role")