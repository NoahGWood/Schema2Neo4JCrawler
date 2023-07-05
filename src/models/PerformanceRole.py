from pydantic import BaseModel
from models.Role import Role

from typing import Optional, Any

class PerformanceRole(Role):
    characterName: Optional[Any] = None

