from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class ArchiveComponent(CreativeWork):
    holdingArchive: Optional[Any] = None
    itemLocation: Optional[Any] = None
