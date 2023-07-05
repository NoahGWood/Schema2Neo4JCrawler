from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ProgramMembership(Thing):
    hostingOrganization: Optional[Any] = None
    member: Optional[Any] = None
    membershipNumber: Optional[Any] = None
    membershipPointsEarned: Optional[Any] = None
    programName: Optional[Any] = None

