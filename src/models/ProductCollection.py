from pydantic import BaseModel
from models.Collection import Collection

from typing import Optional, Any

class ProductCollection(Collection):
    includesObject: Optional[Any] = None

