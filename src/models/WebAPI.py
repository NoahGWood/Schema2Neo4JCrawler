from pydantic import BaseModel
from models.Service import Service

from typing import Optional, Any

class WebAPI(Service):
    documentation: Optional[Any] = None

