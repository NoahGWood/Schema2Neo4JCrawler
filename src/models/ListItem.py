from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ListItem(Thing):
    item: Optional[Any] = None
    nextItem: Optional[Any] = None
    position: Optional[Any] = None
    previousItem: Optional[Any] = None

