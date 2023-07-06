from pydantic import BaseModel
from typing import Optional, Any

class MedicalObservationalStudyDesign(BaseModel):
    studyDesign: Optional[Any] = None

