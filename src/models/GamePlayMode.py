from pydantic import BaseModel
from typing import Optional, Any

class GamePlayMode(BaseModel):
    playMode: Optional[Any] = None

