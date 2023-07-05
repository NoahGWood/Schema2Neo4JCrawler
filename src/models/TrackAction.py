from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class TrackAction(Action):
    deliveryMethod: Optional[Any] = None

