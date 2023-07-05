from pydantic import BaseModel
from models.Event import Event

from typing import Optional, Any

class SportsEvent(Event):
    awayTeam: Optional[Any] = None
    competitor: Optional[Any] = None
    homeTeam: Optional[Any] = None
    sport: Optional[Any] = None

