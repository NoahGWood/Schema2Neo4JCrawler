from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class ComicSeries(CreativeWork):
    endDate: Optional[Any] = None
    issn: Optional[Any] = None
    startDate: Optional[Any] = None

