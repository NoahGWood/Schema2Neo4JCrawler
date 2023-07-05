from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class DefinedTerm(Thing):
    inDefinedTermSet: Optional[Any] = None
    termCode: Optional[Any] = None

