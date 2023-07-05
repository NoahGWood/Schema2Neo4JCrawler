from pydantic import BaseModel
from models.Review import Review

from typing import Optional, Any

class Recommendation(Review):
    category: Optional[Any] = None

