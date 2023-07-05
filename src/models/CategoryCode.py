from pydantic import BaseModel
from models.DefinedTerm import DefinedTerm

from typing import Optional, Any

class CategoryCode(DefinedTerm):
    codeValue: Optional[Any] = None
    inCodeSet: Optional[Any] = None

