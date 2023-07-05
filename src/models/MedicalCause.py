from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalCause(MedicalEntity):
    causeOf: Optional[Any] = None

