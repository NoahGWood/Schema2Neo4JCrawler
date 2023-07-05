from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Collection(CreativeWork):
    collectionSize: Optional[Any] = None

