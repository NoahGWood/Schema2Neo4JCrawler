from pydantic import BaseModel
from models.CreativeWorkSeries import CreativeWorkSeries

from typing import Optional, Any

class TVSeries(CreativeWorkSeries):
    actor: Optional[Any] = None
    containsSeason: Optional[Any] = None
    countryOfOrigin: Optional[Any] = None
    director: Optional[Any] = None
    episode: Optional[Any] = None
    musicBy: Optional[Any] = None
    numberOfEpisodes: Optional[Any] = None
    numberOfSeasons: Optional[Any] = None
    productionCompany: Optional[Any] = None
    titleEIDR: Optional[Any] = None
    trailer: Optional[Any] = None

