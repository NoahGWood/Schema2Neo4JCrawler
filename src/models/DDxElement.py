from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class DDxElement(MedicalEntity):
    diagnosis: Optional[Any] = None
    distinguishingSign: Optional[Any] = None

