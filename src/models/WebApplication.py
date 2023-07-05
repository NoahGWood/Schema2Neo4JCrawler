from pydantic import BaseModel
from models.SoftwareApplication import SoftwareApplication

from typing import Optional, Any

class WebApplication(SoftwareApplication):
    browserRequirements: Optional[Any] = None

