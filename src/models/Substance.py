from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class Substance(MedicalEntity):
    activeIngredient: Optional[Any] = None
    maximumIntake: Optional[Any] = None

