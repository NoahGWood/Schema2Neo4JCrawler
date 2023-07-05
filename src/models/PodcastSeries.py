from pydantic import BaseModel
from models.CreativeWorkSeries import CreativeWorkSeries

from typing import Optional, Any

class PodcastSeries(CreativeWorkSeries):
    actor: Optional[Any] = None
    webFeed: Optional[Any] = None

