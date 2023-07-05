from pydantic import BaseModel
from models.UpdateAction import UpdateAction

from typing import Optional, Any

class PrependAction(UpdateAction):
    toLocation: Optional[Any] = None

