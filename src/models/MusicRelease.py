from pydantic import BaseModel
from models.MusicPlaylist import MusicPlaylist

from typing import Optional, Any

class MusicRelease(MusicPlaylist):
    catalogNumber: Optional[Any] = None
    creditedTo: Optional[Any] = None
    duration: Optional[Any] = None
    musicReleaseFormat: Optional[Any] = None
    recordLabel: Optional[Any] = None
    releaseOf: Optional[Any] = None

