from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class SuperficialAnatomy(MedicalEntity):
    associatedPathophysiology: Optional[Any] = None
    relatedAnatomy: Optional[Any] = None
    relatedCondition: Optional[Any] = None
    relatedTherapy: Optional[Any] = None
    significance: Optional[Any] = None

