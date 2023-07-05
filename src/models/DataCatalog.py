from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class DataCatalog(CreativeWork):
    dataset: Optional[Any] = None
    measurementMethod: Optional[Any] = None
    measurementTechnique: Optional[Any] = None

