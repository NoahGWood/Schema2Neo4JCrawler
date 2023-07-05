from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Blog(CreativeWork):
    blogPost: Optional[Any] = None
    issn: Optional[Any] = None

