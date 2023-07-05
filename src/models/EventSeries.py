from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class EventSeries(Thing):
    about: Optional[Any] = None
    actor: Optional[Any] = None
    aggregateRating: Optional[Any] = None
    attendee: Optional[Any] = None
    audience: Optional[Any] = None
    composer: Optional[Any] = None
    contributor: Optional[Any] = None
    director: Optional[Any] = None
    doorTime: Optional[Any] = None
    duration: Optional[Any] = None
    endDate: Optional[Any] = None
    eventAttendanceMode: Optional[Any] = None
    eventSchedule: Optional[Any] = None
    eventStatus: Optional[Any] = None
    funder: Optional[Any] = None
    funding: Optional[Any] = None
    inLanguage: Optional[Any] = None
    isAccessibleForFree: Optional[Any] = None
    keywords: Optional[Any] = None
    location: Optional[Any] = None
    maximumAttendeeCapacity: Optional[Any] = None
    maximumPhysicalAttendeeCapacity: Optional[Any] = None
    maximumVirtualAttendeeCapacity: Optional[Any] = None
    offers: Optional[Any] = None
    organizer: Optional[Any] = None
    performer: Optional[Any] = None
    previousStartDate: Optional[Any] = None
    recordedIn: Optional[Any] = None
    remainingAttendeeCapacity: Optional[Any] = None
    review: Optional[Any] = None
    sponsor: Optional[Any] = None
    startDate: Optional[Any] = None
    subEvent: Optional[Any] = None
    superEvent: Optional[Any] = None
    translator: Optional[Any] = None
    typicalAgeRange: Optional[Any] = None
    workFeatured: Optional[Any] = None
    workPerformed: Optional[Any] = None

