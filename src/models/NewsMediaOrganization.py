from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class NewsMediaOrganization(Organization):
    actionableFeedbackPolicy: Optional[Any] = None
    correctionsPolicy: Optional[Any] = None
    diversityPolicy: Optional[Any] = None
    diversityStaffingReport: Optional[Any] = None
    ethicsPolicy: Optional[Any] = None
    masthead: Optional[Any] = None
    missionCoveragePrioritiesPolicy: Optional[Any] = None
    noBylinesPolicy: Optional[Any] = None
    ownershipFundingInfo: Optional[Any] = None
    unnamedSourcesPolicy: Optional[Any] = None
    verificationFactCheckingPolicy: Optional[Any] = None

