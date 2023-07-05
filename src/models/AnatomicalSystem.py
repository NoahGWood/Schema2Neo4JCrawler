from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class AnatomicalSystem(MedicalEntity):
    associatedPathophysiology: Optional[Any] = None
    comprisedOf: Optional[Any] = None
    relatedCondition: Optional[Any] = None
    relatedStructure: Optional[Any] = None
    relatedTherapy: Optional[Any] = None

