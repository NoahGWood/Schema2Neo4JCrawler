from pydantic import BaseModel
from models.Game import Game

from typing import Optional, Any

class VideoGame(Game):
    actor: Optional[Any] = None
    cheatCode: Optional[Any] = None
    director: Optional[Any] = None
    gameEdition: Optional[Any] = None
    gamePlatform: Optional[Any] = None
    gameServer: Optional[Any] = None
    gameTip: Optional[Any] = None
    musicBy: Optional[Any] = None
    playMode: Optional[Any] = None
    trailer: Optional[Any] = None

