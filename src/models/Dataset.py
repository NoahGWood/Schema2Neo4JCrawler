from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Dataset(CreativeWork):
    distribution: Optional[Any] = None
    includedInDataCatalog: Optional[Any] = None
    issn: Optional[Any] = None
    measurementMethod: Optional[Any] = None
    measurementTechnique: Optional[Any] = None
    variableMeasured: Optional[Any] = None

