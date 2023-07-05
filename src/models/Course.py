from pydantic import BaseModel
from models.LearningResource import LearningResource

from typing import Optional, Any

class Course(LearningResource):
    availableLanguage: Optional[Any] = None
    courseCode: Optional[Any] = None
    coursePrerequisites: Optional[Any] = None
    educationalCredentialAwarded: Optional[Any] = None
    financialAidEligible: Optional[Any] = None
    hasCourseInstance: Optional[Any] = None
    numberOfCredits: Optional[Any] = None
    occupationalCredentialAwarded: Optional[Any] = None
    syllabusSections: Optional[Any] = None
    totalHistoricalEnrollment: Optional[Any] = None

