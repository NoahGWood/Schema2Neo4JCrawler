from pydantic import BaseModel
from typing import Optional, Any

class DigitalDocumentPermissionType(BaseModel):
    permissionType: Optional[Any] = None

