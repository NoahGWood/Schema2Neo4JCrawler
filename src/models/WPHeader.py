from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class WPHeader(CreativeWork):
    cssSelector: Optional[Any] = None
    xpath: Optional[Any] = None

