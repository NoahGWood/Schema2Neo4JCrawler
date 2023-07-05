from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class MusicGroup(Organization):
    album: Optional[Any] = None
    genre: Optional[Any] = None
    track: Optional[Any] = None

