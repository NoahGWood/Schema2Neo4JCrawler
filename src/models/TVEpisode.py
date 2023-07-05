from pydantic import BaseModel
from models.Episode import Episode

from typing import Optional, Any

class TVEpisode(Episode):
    countryOfOrigin: Optional[Any] = None
    subtitleLanguage: Optional[Any] = None
    titleEIDR: Optional[Any] = None

