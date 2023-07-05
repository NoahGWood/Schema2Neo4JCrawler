from pydantic import BaseModel
from models.CommunicateAction import CommunicateAction

from typing import Optional, Any

class CommentAction(CommunicateAction):
    resultComment: Optional[Any] = None

