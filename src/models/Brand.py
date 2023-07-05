from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Brand(Thing):
    aggregateRating: Optional[Any] = None
    logo: Optional[Any] = None
    review: Optional[Any] = None
    slogan: Optional[Any] = None

