from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class QAPage(CreativeWork):
    breadcrumb: Optional[Any] = None
    lastReviewed: Optional[Any] = None
    mainContentOfPage: Optional[Any] = None
    primaryImageOfPage: Optional[Any] = None
    relatedLink: Optional[Any] = None
    reviewedBy: Optional[Any] = None
    significantLink: Optional[Any] = None
    speakable: Optional[Any] = None
    specialty: Optional[Any] = None

