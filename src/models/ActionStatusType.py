from pydantic import BaseModel
from typing import Optional, Any

class ActionStatusType(BaseModel):
    actionStatus: Optional[Any] = None

