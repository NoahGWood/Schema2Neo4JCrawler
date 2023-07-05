from pydantic import BaseModel
from models.Role import Role

from typing import Optional, Any

class LinkRole(Role):
    inLanguage: Optional[Any] = None
    linkRelationship: Optional[Any] = None

