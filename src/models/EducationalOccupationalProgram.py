from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class EducationalOccupationalProgram(Thing):
    applicationDeadline: Optional[Any] = None
    applicationStartDate: Optional[Any] = None
    dayOfWeek: Optional[Any] = None
    educationalCredentialAwarded: Optional[Any] = None
    educationalProgramMode: Optional[Any] = None
    endDate: Optional[Any] = None
    financialAidEligible: Optional[Any] = None
    hasCourse: Optional[Any] = None
    maximumEnrollment: Optional[Any] = None
    numberOfCredits: Optional[Any] = None
    occupationalCategory: Optional[Any] = None
    occupationalCredentialAwarded: Optional[Any] = None
    offers: Optional[Any] = None
    programPrerequisites: Optional[Any] = None
    programType: Optional[Any] = None
    provider: Optional[Any] = None
    salaryUponCompletion: Optional[Any] = None
    startDate: Optional[Any] = None
    termDuration: Optional[Any] = None
    termsPerYear: Optional[Any] = None
    timeOfDay: Optional[Any] = None
    timeToComplete: Optional[Any] = None
    trainingSalary: Optional[Any] = None
    typicalCreditsPerTerm: Optional[Any] = None

