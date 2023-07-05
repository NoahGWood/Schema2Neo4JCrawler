from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class PublicationIssue(CreativeWork):
    issueNumber: Optional[Any] = None
    pageEnd: Optional[Any] = None
    pageStart: Optional[Any] = None
    pagination: Optional[Any] = None

