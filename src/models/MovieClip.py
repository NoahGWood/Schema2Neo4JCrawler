from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class MovieClip(CreativeWork):
    actor: Optional[Any] = None
    clipNumber: Optional[Any] = None
    director: Optional[Any] = None
    endOffset: Optional[Any] = None
    musicBy: Optional[Any] = None
    partOfEpisode: Optional[Any] = None
    partOfSeason: Optional[Any] = None
    partOfSeries: Optional[Any] = None
    startOffset: Optional[Any] = None

