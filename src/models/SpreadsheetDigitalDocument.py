from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class SpreadsheetDigitalDocument(CreativeWork):
    hasDigitalDocumentPermission: Optional[Any] = None

