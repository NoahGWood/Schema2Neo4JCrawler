from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Researcher(Thing):
    audienceType: Optional[Any] = None
    geographicArea: Optional[Any] = None

