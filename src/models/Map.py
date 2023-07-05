from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Map(CreativeWork):
    mapType: Optional[Any] = None

