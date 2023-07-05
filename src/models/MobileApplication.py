from pydantic import BaseModel
from models.SoftwareApplication import SoftwareApplication

from typing import Optional, Any

class MobileApplication(SoftwareApplication):
    carrierRequirements: Optional[Any] = None

