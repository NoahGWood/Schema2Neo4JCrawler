from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class MenuSection(CreativeWork):
    hasMenuItem: Optional[Any] = None
    hasMenuSection: Optional[Any] = None

