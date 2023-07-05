from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class GameServer(Thing):
    game: Optional[Any] = None
    playersOnline: Optional[Any] = None
    serverStatus: Optional[Any] = None

