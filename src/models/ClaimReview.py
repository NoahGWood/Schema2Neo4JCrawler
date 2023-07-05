from pydantic import BaseModel
from models.Review import Review

from typing import Optional, Any

class ClaimReview(Review):
    claimReviewed: Optional[Any] = None

