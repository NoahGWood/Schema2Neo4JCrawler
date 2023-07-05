from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class MusicRecording(CreativeWork):
    byArtist: Optional[Any] = None
    duration: Optional[Any] = None
    inAlbum: Optional[Any] = None
    inPlaylist: Optional[Any] = None
    isrcCode: Optional[Any] = None
    recordingOf: Optional[Any] = None

