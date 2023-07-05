from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class EntryPoint(Thing):
    actionApplication: Optional[Any] = None
    actionPlatform: Optional[Any] = None
    contentType: Optional[Any] = None
    encodingType: Optional[Any] = None
    httpMethod: Optional[Any] = None
    urlTemplate: Optional[Any] = None

