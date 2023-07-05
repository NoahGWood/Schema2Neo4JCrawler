from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class AlignmentObject(Thing):
    alignmentType: Optional[Any] = None
    educationalFramework: Optional[Any] = None
    targetDescription: Optional[Any] = None
    targetName: Optional[Any] = None
    targetUrl: Optional[Any] = None

