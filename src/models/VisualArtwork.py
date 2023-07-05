from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class VisualArtwork(CreativeWork):
    artEdition: Optional[Any] = None
    artMedium: Optional[Any] = None
    artform: Optional[Any] = None
    artist: Optional[Any] = None
    artworkSurface: Optional[Any] = None
    colorist: Optional[Any] = None
    depth: Optional[Any] = None
    height: Optional[Any] = None
    inker: Optional[Any] = None
    letterer: Optional[Any] = None
    penciler: Optional[Any] = None
    width: Optional[Any] = None

