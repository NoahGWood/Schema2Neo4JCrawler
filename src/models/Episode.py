from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Episode(CreativeWork):
    actor: Optional[Any] = None
    director: Optional[Any] = None
    duration: Optional[Any] = None
    episodeNumber: Optional[Any] = None
    musicBy: Optional[Any] = None
    partOfSeason: Optional[Any] = None
    partOfSeries: Optional[Any] = None
    productionCompany: Optional[Any] = None
    trailer: Optional[Any] = None

