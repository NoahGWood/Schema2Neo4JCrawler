from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class SpecialAnnouncement(CreativeWork):
    announcementLocation: Optional[Any] = None
    category: Optional[Any] = None
    datePosted: Optional[Any] = None
    diseasePreventionInfo: Optional[Any] = None
    diseaseSpreadStatistics: Optional[Any] = None
    gettingTestedInfo: Optional[Any] = None
    governmentBenefitsInfo: Optional[Any] = None
    newsUpdatesAndGuidelines: Optional[Any] = None
    publicTransportClosuresInfo: Optional[Any] = None
    quarantineGuidelines: Optional[Any] = None
    schoolClosuresInfo: Optional[Any] = None
    travelBans: Optional[Any] = None
    webFeed: Optional[Any] = None

