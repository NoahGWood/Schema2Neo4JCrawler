from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Comment(CreativeWork):
    downvoteCount: Optional[Any] = None
    parentItem: Optional[Any] = None
    upvoteCount: Optional[Any] = None

