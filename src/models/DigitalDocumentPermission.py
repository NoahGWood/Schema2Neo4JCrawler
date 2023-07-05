from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class DigitalDocumentPermission(Thing):
    grantee: Optional[Any] = None
    permissionType: Optional[Any] = None

