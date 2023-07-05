from pydantic import BaseModel
from models.MedicalStudy import MedicalStudy

from typing import Optional, Any

class MedicalObservationalStudy(MedicalStudy):
    studyDesign: Optional[Any] = None

