from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class GeospatialGeometry(Thing):
    geoContains: Optional[Any] = None
    geoCoveredBy: Optional[Any] = None
    geoCovers: Optional[Any] = None
    geoCrosses: Optional[Any] = None
    geoDisjoint: Optional[Any] = None
    geoEquals: Optional[Any] = None
    geoIntersects: Optional[Any] = None
    geoOverlaps: Optional[Any] = None
    geoTouches: Optional[Any] = None
    geoWithin: Optional[Any] = None

