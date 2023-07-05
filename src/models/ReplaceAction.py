from pydantic import BaseModel
from models.UpdateAction import UpdateAction

from typing import Optional, Any

class ReplaceAction(UpdateAction):
    replacee: Optional[Any] = None
    replacer: Optional[Any] = None

