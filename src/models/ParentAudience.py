from pydantic import BaseModel
from models.PeopleAudience import PeopleAudience

from typing import Optional, Any

class ParentAudience(PeopleAudience):
    childMaxAge: Optional[Any] = None
    childMinAge: Optional[Any] = None

