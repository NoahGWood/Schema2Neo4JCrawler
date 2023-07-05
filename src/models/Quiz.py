from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Quiz(CreativeWork):
    assesses: Optional[Any] = None
    competencyRequired: Optional[Any] = None
    educationalAlignment: Optional[Any] = None
    educationalLevel: Optional[Any] = None
    educationalUse: Optional[Any] = None
    learningResourceType: Optional[Any] = None
    teaches: Optional[Any] = None

