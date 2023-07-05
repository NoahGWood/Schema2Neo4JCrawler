from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class ExercisePlan(CreativeWork):
    activityDuration: Optional[Any] = None
    activityFrequency: Optional[Any] = None
    additionalVariable: Optional[Any] = None
    exerciseType: Optional[Any] = None
    intensity: Optional[Any] = None
    repetitions: Optional[Any] = None
    restPeriods: Optional[Any] = None
    workload: Optional[Any] = None

