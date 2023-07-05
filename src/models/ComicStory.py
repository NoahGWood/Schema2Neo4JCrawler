from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class ComicStory(CreativeWork):
    artist: Optional[Any] = None
    colorist: Optional[Any] = None
    inker: Optional[Any] = None
    letterer: Optional[Any] = None
    penciler: Optional[Any] = None

