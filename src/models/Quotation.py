from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Quotation(CreativeWork):
    spokenByCharacter: Optional[Any] = None

