from pydantic import BaseModel
from models.NewsArticle import NewsArticle

from typing import Optional, Any

class ReviewNewsArticle(NewsArticle):
    associatedClaimReview: Optional[Any] = None
    associatedMediaReview: Optional[Any] = None
    associatedReview: Optional[Any] = None
    itemReviewed: Optional[Any] = None
    negativeNotes: Optional[Any] = None
    positiveNotes: Optional[Any] = None
    reviewAspect: Optional[Any] = None
    reviewBody: Optional[Any] = None
    reviewRating: Optional[Any] = None

