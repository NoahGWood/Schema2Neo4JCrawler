from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ActivateAction(Thing):
    actionStatus: Optional[Any] = None
    agent: Optional[Any] = None
    endTime: Optional[Any] = None
    error: Optional[Any] = None
    instrument: Optional[Any] = None
    location: Optional[Any] = None
    object: Optional[Any] = None
    participant: Optional[Any] = None
    provider: Optional[Any] = None
    result: Optional[Any] = None
    startTime: Optional[Any] = None
    target: Optional[Any] = None

