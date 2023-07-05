from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class SportsOrganization(Organization):
    sport: Optional[Any] = None

