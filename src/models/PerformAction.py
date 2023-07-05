from pydantic import BaseModel
from models.PlayAction import PlayAction

from typing import Optional, Any

class PerformAction(PlayAction):
    entertainmentBusiness: Optional[Any] = None

