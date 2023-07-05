from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class ArchiveOrganization(LocalBusiness):
    archiveHeld: Optional[Any] = None

