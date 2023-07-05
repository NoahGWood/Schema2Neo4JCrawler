from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Role(Thing):
    endDate: Optional[Any] = None
    roleName: Optional[Any] = None
    startDate: Optional[Any] = None

