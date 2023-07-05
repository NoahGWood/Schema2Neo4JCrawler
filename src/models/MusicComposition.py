from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class MusicComposition(CreativeWork):
    composer: Optional[Any] = None
    firstPerformance: Optional[Any] = None
    includedComposition: Optional[Any] = None
    iswcCode: Optional[Any] = None
    lyricist: Optional[Any] = None
    lyrics: Optional[Any] = None
    musicArrangement: Optional[Any] = None
    musicCompositionForm: Optional[Any] = None
    musicalKey: Optional[Any] = None
    recordedAs: Optional[Any] = None

