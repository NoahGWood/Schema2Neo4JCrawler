from pydantic import BaseModel
from models.VisualArtwork import VisualArtwork

from typing import Optional, Any

class ComicCoverArt(VisualArtwork):
    artist: Optional[Any] = None
    colorist: Optional[Any] = None
    inker: Optional[Any] = None
    letterer: Optional[Any] = None
    penciler: Optional[Any] = None

