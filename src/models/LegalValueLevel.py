from pydantic import BaseModel
from typing import Optional, Any

class LegalValueLevel(BaseModel):
    legislationLegalValue: Optional[Any] = None

