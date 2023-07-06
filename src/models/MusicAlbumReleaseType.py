from pydantic import BaseModel
from typing import Optional, Any

class MusicAlbumReleaseType(BaseModel):
    albumReleaseType: Optional[Any] = None

