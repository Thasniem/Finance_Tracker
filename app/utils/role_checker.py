from fastapi import Header, HTTPException

def get_role(x_role: str | None = Header(default=None, alias="X-Role")):
    """
    Extract user role from X-Role header.
    If not provided, default to 'viewer' for browser access.
    """
    if not x_role:
        return "viewer"
    return x_role.lower()


# Only admin allowed
def require_admin(role: str):
    """
    Allow access only to admin users.
    """
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")


# Admin + Analyst allowed
def require_analyst_or_admin(role: str):
    """
    Allow access to admin and analyst roles.
    """
    if role not in ["admin", "analyst"]:
        raise HTTPException(status_code=403, detail="Access denied")


# Viewer, Analyst, Admin allowed (for read-only)
def require_any_role(role: str):
    """
    Allow access to all valid roles.
    """
    if role not in ["admin", "analyst", "viewer"]:
        raise HTTPException(status_code=403, detail="Invalid role")