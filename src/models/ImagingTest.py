from pydantic import BaseModel
from models.MedicalTest import MedicalTest

from typing import Optional, Any

class ImagingTest(MedicalTest):
    imagingTechnique: Optional[Any] = None

