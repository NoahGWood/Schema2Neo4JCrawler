from pydantic import BaseModel
from models.CreativeWorkSeries import CreativeWorkSeries

from typing import Optional, Any

class VideoGameSeries(CreativeWorkSeries):
    actor: Optional[Any] = None
    characterAttribute: Optional[Any] = None
    cheatCode: Optional[Any] = None
    containsSeason: Optional[Any] = None
    director: Optional[Any] = None
    episode: Optional[Any] = None
    gameItem: Optional[Any] = None
    gameLocation: Optional[Any] = None
    gamePlatform: Optional[Any] = None
    musicBy: Optional[Any] = None
    numberOfEpisodes: Optional[Any] = None
    numberOfPlayers: Optional[Any] = None
    numberOfSeasons: Optional[Any] = None
    playMode: Optional[Any] = None
    productionCompany: Optional[Any] = None
    quest: Optional[Any] = None
    trailer: Optional[Any] = None

