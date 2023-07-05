from pydantic import BaseModel
from models.Audience import Audience

from typing import Optional, Any

class EducationalAudience(Audience):
    educationalRole: Optional[Any] = None

