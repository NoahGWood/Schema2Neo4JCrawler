from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Game(CreativeWork):
    characterAttribute: Optional[Any] = None
    gameItem: Optional[Any] = None
    gameLocation: Optional[Any] = None
    numberOfPlayers: Optional[Any] = None
    quest: Optional[Any] = None

