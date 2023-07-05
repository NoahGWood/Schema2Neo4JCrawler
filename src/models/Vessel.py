from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class Vessel(MedicalEntity):
    associatedPathophysiology: Optional[Any] = None
    bodyLocation: Optional[Any] = None
    connectedTo: Optional[Any] = None
    diagram: Optional[Any] = None
    partOfSystem: Optional[Any] = None
    relatedCondition: Optional[Any] = None
    relatedTherapy: Optional[Any] = None
    subStructure: Optional[Any] = None

