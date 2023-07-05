from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Movie(CreativeWork):
    actor: Optional[Any] = None
    countryOfOrigin: Optional[Any] = None
    director: Optional[Any] = None
    duration: Optional[Any] = None
    musicBy: Optional[Any] = None
    productionCompany: Optional[Any] = None
    subtitleLanguage: Optional[Any] = None
    titleEIDR: Optional[Any] = None
    trailer: Optional[Any] = None

