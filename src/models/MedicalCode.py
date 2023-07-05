from pydantic import BaseModel
from models.CategoryCode import CategoryCode

from typing import Optional, Any

class MedicalCode(CategoryCode):
    codeValue: Optional[Any] = None
    codingSystem: Optional[Any] = None

