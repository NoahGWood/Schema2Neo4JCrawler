from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalDevice(MedicalEntity):
    adverseOutcome: Optional[Any] = None
    contraindication: Optional[Any] = None
    postOp: Optional[Any] = None
    preOp: Optional[Any] = None
    procedure: Optional[Any] = None
    seriousAdverseOutcome: Optional[Any] = None

