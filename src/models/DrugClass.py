from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class DrugClass(MedicalEntity):
    drug: Optional[Any] = None

