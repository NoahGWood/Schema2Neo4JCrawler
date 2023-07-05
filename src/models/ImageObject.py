from pydantic import BaseModel
from models.MediaObject import MediaObject

from typing import Optional, Any

class ImageObject(MediaObject):
    caption: Optional[Any] = None
    embeddedTextCaption: Optional[Any] = None
    exifData: Optional[Any] = None
    representativeOfPage: Optional[Any] = None

