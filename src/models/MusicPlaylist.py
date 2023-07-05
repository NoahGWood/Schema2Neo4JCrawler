from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class MusicPlaylist(CreativeWork):
    numTracks: Optional[Any] = None
    track: Optional[Any] = None

