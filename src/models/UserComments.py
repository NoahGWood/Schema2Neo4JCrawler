from pydantic import BaseModel
from models.Event import Event

from typing import Optional, Any

class UserComments(Event):
    commentText: Optional[Any] = None
    commentTime: Optional[Any] = None
    creator: Optional[Any] = None
    discusses: Optional[Any] = None
    replyToUrl: Optional[Any] = None

