from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Grant(Thing):
    fundedItem: Optional[Any] = None
    funder: Optional[Any] = None
    sponsor: Optional[Any] = None

