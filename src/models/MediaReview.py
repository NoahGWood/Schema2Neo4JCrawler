from pydantic import BaseModel
from models.Review import Review

from typing import Optional, Any

class MediaReview(Review):
    mediaAuthenticityCategory: Optional[Any] = None
    originalMediaContextDescription: Optional[Any] = None
    originalMediaLink: Optional[Any] = None

