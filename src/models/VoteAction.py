from pydantic import BaseModel
from models.ChooseAction import ChooseAction

from typing import Optional, Any

class VoteAction(ChooseAction):
    candidate: Optional[Any] = None

