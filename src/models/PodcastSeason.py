from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class PodcastSeason(CreativeWork):
    actor: Optional[Any] = None
    director: Optional[Any] = None
    endDate: Optional[Any] = None
    episode: Optional[Any] = None
    numberOfEpisodes: Optional[Any] = None
    partOfSeries: Optional[Any] = None
    productionCompany: Optional[Any] = None
    seasonNumber: Optional[Any] = None
    startDate: Optional[Any] = None
    trailer: Optional[Any] = None

