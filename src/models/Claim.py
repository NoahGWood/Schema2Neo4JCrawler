from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Claim(CreativeWork):
    appearance: Optional[Any] = None
    claimInterpreter: Optional[Any] = None
    firstAppearance: Optional[Any] = None

