from pydantic import BaseModel
from models.MediaObject import MediaObject

from typing import Optional, Any

class VideoObject(MediaObject):
    actor: Optional[Any] = None
    caption: Optional[Any] = None
    director: Optional[Any] = None
    embeddedTextCaption: Optional[Any] = None
    musicBy: Optional[Any] = None
    transcript: Optional[Any] = None
    videoFrameSize: Optional[Any] = None
    videoQuality: Optional[Any] = None

