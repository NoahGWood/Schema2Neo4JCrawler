from pydantic import BaseModel
from models.MediaObject import MediaObject

from typing import Optional, Any

class AudioObject(MediaObject):
    caption: Optional[Any] = None
    embeddedTextCaption: Optional[Any] = None
    transcript: Optional[Any] = None

