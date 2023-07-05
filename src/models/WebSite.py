from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class WebSite(CreativeWork):
    issn: Optional[Any] = None

