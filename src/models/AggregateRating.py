from pydantic import BaseModel
from models.Rating import Rating

from typing import Optional, Any

class AggregateRating(Rating):
    itemReviewed: Optional[Any] = None
    ratingCount: Optional[Any] = None
    reviewCount: Optional[Any] = None

