from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class SearchAction(Action):
    query: Optional[Any] = None

