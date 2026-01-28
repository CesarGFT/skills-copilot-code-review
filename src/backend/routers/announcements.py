"""
Endpoints for managing announcements
"""

from fastapi import APIRouter, Body
from typing import Dict, Any

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"]
)


# In-memory announcement storage (you could replace with database)
# TODO: Persist announcements to database for production use
current_announcement: Dict[str, Any] = {
    "message": "Welcome to Mergington High School! Check out our extracurricular activities."
}


@router.get("", response_model=Dict[str, Any])
def get_announcement() -> Dict[str, Any]:
    """
    Get the current announcement banner message
    """
    return current_announcement


@router.post("", response_model=Dict[str, Any])
def set_announcement(body: Dict[str, str] = Body(...)) -> Dict[str, Any]:
    """
    Set a new announcement banner message (admin only in production)
    
    - body: JSON object with "message" field containing the announcement text
    """
    global current_announcement
    message = body.get("message", "")
    if not message:
        return {"status": "error", "message": "Message cannot be empty"}
    current_announcement = {"message": message}
    return {"status": "success", "message": message}
