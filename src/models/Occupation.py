from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Occupation(Thing):
    educationRequirements: Optional[Any] = None
    estimatedSalary: Optional[Any] = None
    experienceRequirements: Optional[Any] = None
    occupationLocation: Optional[Any] = None
    occupationalCategory: Optional[Any] = None
    qualifications: Optional[Any] = None
    responsibilities: Optional[Any] = None
    skills: Optional[Any] = None

