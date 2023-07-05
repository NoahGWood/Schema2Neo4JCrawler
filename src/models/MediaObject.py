from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class MediaObject(CreativeWork):
    associatedArticle: Optional[Any] = None
    bitrate: Optional[Any] = None
    contentSize: Optional[Any] = None
    contentUrl: Optional[Any] = None
    duration: Optional[Any] = None
    embedUrl: Optional[Any] = None
    encodesCreativeWork: Optional[Any] = None
    encodingFormat: Optional[Any] = None
    endTime: Optional[Any] = None
    height: Optional[Any] = None
    ineligibleRegion: Optional[Any] = None
    interpretedAsClaim: Optional[Any] = None
    playerType: Optional[Any] = None
    productionCompany: Optional[Any] = None
    regionsAllowed: Optional[Any] = None
    requiresSubscription: Optional[Any] = None
    sha256: Optional[Any] = None
    startTime: Optional[Any] = None
    uploadDate: Optional[Any] = None
    width: Optional[Any] = None

