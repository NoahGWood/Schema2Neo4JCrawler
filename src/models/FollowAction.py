from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class FollowAction(Action):
    followee: Optional[Any] = None

