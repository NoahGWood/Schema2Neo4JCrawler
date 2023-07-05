from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class PhysicalActivity(MedicalEntity):
    associatedAnatomy: Optional[Any] = None
    category: Optional[Any] = None
    epidemiology: Optional[Any] = None
    pathophysiology: Optional[Any] = None

