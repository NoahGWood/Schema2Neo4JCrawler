from pydantic import BaseModel
from models.UpdateAction import UpdateAction

from typing import Optional, Any

class AppendAction(UpdateAction):
    toLocation: Optional[Any] = None

