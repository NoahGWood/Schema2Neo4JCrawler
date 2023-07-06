from pydantic import BaseModel
from typing import Optional, Any

class MusicReleaseFormatType(BaseModel):
    musicReleaseFormat: Optional[Any] = None

