from pydantic import BaseModel
from models.PlayAction import PlayAction

from typing import Optional, Any

class ExerciseAction(PlayAction):
    diet: Optional[Any] = None
    distance: Optional[Any] = None
    exerciseCourse: Optional[Any] = None
    exercisePlan: Optional[Any] = None
    exerciseRelatedDiet: Optional[Any] = None
    exerciseType: Optional[Any] = None
    fromLocation: Optional[Any] = None
    opponent: Optional[Any] = None
    sportsActivityLocation: Optional[Any] = None
    sportsEvent: Optional[Any] = None
    sportsTeam: Optional[Any] = None
    toLocation: Optional[Any] = None

