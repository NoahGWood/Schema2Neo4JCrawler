from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class TextDigitalDocument(CreativeWork):
    hasDigitalDocumentPermission: Optional[Any] = None

