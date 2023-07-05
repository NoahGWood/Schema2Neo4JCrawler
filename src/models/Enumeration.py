from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Enumeration(Thing):
    supersededBy: Optional[Any] = None

