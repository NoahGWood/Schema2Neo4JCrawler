from pydantic import BaseModel
from models.CommunicateAction import CommunicateAction

from typing import Optional, Any

class InviteAction(CommunicateAction):
    event: Optional[Any] = None

