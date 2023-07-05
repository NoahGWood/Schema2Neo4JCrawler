from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class AdministrativeArea(Thing):
    additionalProperty: Optional[Any] = None
    address: Optional[Any] = None
    aggregateRating: Optional[Any] = None
    amenityFeature: Optional[Any] = None
    branchCode: Optional[Any] = None
    containedInPlace: Optional[Any] = None
    containsPlace: Optional[Any] = None
    event: Optional[Any] = None
    faxNumber: Optional[Any] = None
    geo: Optional[Any] = None
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
    globalLocationNumber: Optional[Any] = None
    hasDriveThroughService: Optional[Any] = None
    hasMap: Optional[Any] = None
    isAccessibleForFree: Optional[Any] = None
    isicV4: Optional[Any] = None
    keywords: Optional[Any] = None
    latitude: Optional[Any] = None
    logo: Optional[Any] = None
    longitude: Optional[Any] = None
    maximumAttendeeCapacity: Optional[Any] = None
    openingHoursSpecification: Optional[Any] = None
    photo: Optional[Any] = None
    publicAccess: Optional[Any] = None
    review: Optional[Any] = None
    slogan: Optional[Any] = None
    smokingAllowed: Optional[Any] = None
    specialOpeningHoursSpecification: Optional[Any] = None
    telephone: Optional[Any] = None
    tourBookingPage: Optional[Any] = None

