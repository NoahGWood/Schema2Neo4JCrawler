from pydantic import BaseModel
from typing import Optional, Any

class ContactPointOption(BaseModel):
    contactOption: Optional[Any] = None

