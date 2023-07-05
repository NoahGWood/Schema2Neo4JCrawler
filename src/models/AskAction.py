from pydantic import BaseModel
from models.CommunicateAction import CommunicateAction

from typing import Optional, Any

class AskAction(CommunicateAction):
    question: Optional[Any] = None

