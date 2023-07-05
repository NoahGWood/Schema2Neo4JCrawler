from pydantic import BaseModel
from models.PeopleAudience import PeopleAudience

from typing import Optional, Any

class Patient(PeopleAudience):
    diagnosis: Optional[Any] = None
    drug: Optional[Any] = None
    healthCondition: Optional[Any] = None

