from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class ReviewAction(Action):
    resultReview: Optional[Any] = None

