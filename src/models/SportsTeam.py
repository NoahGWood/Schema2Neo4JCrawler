from pydantic import BaseModel
from models.SportsOrganization import SportsOrganization

from typing import Optional, Any

class SportsTeam(SportsOrganization):
    athlete: Optional[Any] = None
    coach: Optional[Any] = None
    gender: Optional[Any] = None

