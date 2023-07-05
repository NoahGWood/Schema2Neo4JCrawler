from pydantic import BaseModel
from models.Legislation import Legislation

from typing import Optional, Any

class LegislationObject(Legislation):
    legislationLegalValue: Optional[Any] = None

