from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class DrugStrength(MedicalEntity):
    activeIngredient: Optional[Any] = None
    availableIn: Optional[Any] = None
    maximumIntake: Optional[Any] = None
    strengthUnit: Optional[Any] = None
    strengthValue: Optional[Any] = None

