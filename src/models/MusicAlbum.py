from pydantic import BaseModel
from models.MusicPlaylist import MusicPlaylist

from typing import Optional, Any

class MusicAlbum(MusicPlaylist):
    albumProductionType: Optional[Any] = None
    albumRelease: Optional[Any] = None
    albumReleaseType: Optional[Any] = None
    byArtist: Optional[Any] = None

