from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class SatiricalArticle(CreativeWork):
    articleBody: Optional[Any] = None
    articleSection: Optional[Any] = None
    backstory: Optional[Any] = None
    pageEnd: Optional[Any] = None
    pageStart: Optional[Any] = None
    pagination: Optional[Any] = None
    speakable: Optional[Any] = None
    wordCount: Optional[Any] = None

