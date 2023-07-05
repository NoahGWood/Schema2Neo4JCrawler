from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalGuidelineContraindication(MedicalEntity):
    evidenceLevel: Optional[Any] = None
    evidenceOrigin: Optional[Any] = None
    guidelineDate: Optional[Any] = None
    guidelineSubject: Optional[Any] = None

