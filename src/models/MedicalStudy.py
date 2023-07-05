from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalStudy(MedicalEntity):
    healthCondition: Optional[Any] = None
    sponsor: Optional[Any] = None
    status: Optional[Any] = None
    studyLocation: Optional[Any] = None
    studySubject: Optional[Any] = None

