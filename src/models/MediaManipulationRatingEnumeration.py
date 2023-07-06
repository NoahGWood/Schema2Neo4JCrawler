from pydantic import BaseModel
from typing import Optional, Any

class MediaManipulationRatingEnumeration(BaseModel):
    mediaAuthenticityCategory: Optional[Any] = None

