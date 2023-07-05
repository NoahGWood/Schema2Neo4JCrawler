from pydantic import BaseModel
from models.AudioObject import AudioObject

from typing import Optional, Any

class Audiobook(AudioObject):
    duration: Optional[Any] = None
    readBy: Optional[Any] = None

