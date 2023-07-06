from pydantic import BaseModel
from typing import Optional, Any

class MusicAlbumProductionType(BaseModel):
    albumProductionType: Optional[Any] = None

