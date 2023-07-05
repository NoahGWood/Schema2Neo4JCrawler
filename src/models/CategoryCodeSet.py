from pydantic import BaseModel
from models.DefinedTermSet import DefinedTermSet

from typing import Optional, Any

class CategoryCodeSet(DefinedTermSet):
    hasCategoryCode: Optional[Any] = None

