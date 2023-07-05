from pydantic import BaseModel
from models.MediaObject import MediaObject

from typing import Optional, Any

class DataDownload(MediaObject):
    measurementMethod: Optional[Any] = None
    measurementTechnique: Optional[Any] = None

