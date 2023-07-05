from pydantic import BaseModel
from models.CommunicateAction import CommunicateAction

from typing import Optional, Any

class ReplyAction(CommunicateAction):
    resultComment: Optional[Any] = None

