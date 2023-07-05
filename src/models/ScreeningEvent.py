from pydantic import BaseModel
from models.Event import Event

from typing import Optional, Any

class ScreeningEvent(Event):
    subtitleLanguage: Optional[Any] = None
    videoFormat: Optional[Any] = None
    workPresented: Optional[Any] = None

