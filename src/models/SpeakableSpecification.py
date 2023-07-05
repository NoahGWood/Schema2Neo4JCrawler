from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class SpeakableSpecification(Thing):
    cssSelector: Optional[Any] = None
    xpath: Optional[Any] = None

