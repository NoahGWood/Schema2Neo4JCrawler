from pydantic import BaseModel
from models.CreativeWorkSeries import CreativeWorkSeries

from typing import Optional, Any

class MovieSeries(CreativeWorkSeries):
    actor: Optional[Any] = None
    director: Optional[Any] = None
    musicBy: Optional[Any] = None
    productionCompany: Optional[Any] = None
    trailer: Optional[Any] = None

