from pydantic import BaseModel
from models.CreativeWorkSeason import CreativeWorkSeason

from typing import Optional, Any

class TVSeason(CreativeWorkSeason):
    countryOfOrigin: Optional[Any] = None
    titleEIDR: Optional[Any] = None

