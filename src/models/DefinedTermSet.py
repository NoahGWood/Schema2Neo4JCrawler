from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class DefinedTermSet(CreativeWork):
    hasDefinedTerm: Optional[Any] = None

