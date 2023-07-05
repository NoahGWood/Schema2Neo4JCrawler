from pydantic import BaseModel
from models.Audience import Audience

from typing import Optional, Any

class PeopleAudience(Audience):
    healthCondition: Optional[Any] = None
    requiredGender: Optional[Any] = None
    requiredMaxAge: Optional[Any] = None
    requiredMinAge: Optional[Any] = None
    suggestedAge: Optional[Any] = None
    suggestedGender: Optional[Any] = None
    suggestedMaxAge: Optional[Any] = None
    suggestedMeasurement: Optional[Any] = None
    suggestedMinAge: Optional[Any] = None

