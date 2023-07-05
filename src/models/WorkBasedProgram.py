from pydantic import BaseModel
from models.EducationalOccupationalProgram import EducationalOccupationalProgram

from typing import Optional, Any

class WorkBasedProgram(EducationalOccupationalProgram):
    occupationalCategory: Optional[Any] = None
    trainingSalary: Optional[Any] = None

