from pydantic import BaseModel
from typing import Optional, Any

class GameServerStatus(BaseModel):
    serverStatus: Optional[Any] = None

