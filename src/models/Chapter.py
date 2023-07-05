from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Chapter(CreativeWork):
    pageEnd: Optional[Any] = None
    pageStart: Optional[Any] = None
    pagination: Optional[Any] = None

