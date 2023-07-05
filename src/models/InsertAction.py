from pydantic import BaseModel
from models.UpdateAction import UpdateAction

from typing import Optional, Any

class InsertAction(UpdateAction):
    toLocation: Optional[Any] = None

