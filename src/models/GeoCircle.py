from pydantic import BaseModel
from models.GeoShape import GeoShape

from typing import Optional, Any

class GeoCircle(GeoShape):
    geoMidpoint: Optional[Any] = None
    geoRadius: Optional[Any] = None

