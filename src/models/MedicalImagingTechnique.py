from pydantic import BaseModel
from typing import Optional, Any

class MedicalImagingTechnique(BaseModel):
    imagingTechnique: Optional[Any] = None

