from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Rating(Thing):
    author: Optional[Any] = None
    bestRating: Optional[Any] = None
    ratingExplanation: Optional[Any] = None
    ratingValue: Optional[Any] = None
    reviewAspect: Optional[Any] = None
    worstRating: Optional[Any] = None

