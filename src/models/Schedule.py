from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Schedule(Thing):
    byDay: Optional[Any] = None
    byMonth: Optional[Any] = None
    byMonthDay: Optional[Any] = None
    byMonthWeek: Optional[Any] = None
    duration: Optional[Any] = None
    endDate: Optional[Any] = None
    endTime: Optional[Any] = None
    exceptDate: Optional[Any] = None
    repeatCount: Optional[Any] = None
    repeatFrequency: Optional[Any] = None
    scheduleTimezone: Optional[Any] = None
    startDate: Optional[Any] = None
    startTime: Optional[Any] = None

