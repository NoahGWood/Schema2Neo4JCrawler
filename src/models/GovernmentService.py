from pydantic import BaseModel
from models.Service import Service

from typing import Optional, Any

class GovernmentService(Service):
    jurisdiction: Optional[Any] = None
    serviceOperator: Optional[Any] = None

