from pydantic import BaseModel
from models.Role import Role

from typing import Optional, Any

class OrganizationRole(Role):
    numberedPosition: Optional[Any] = None

