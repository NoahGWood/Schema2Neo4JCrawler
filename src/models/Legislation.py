from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class Legislation(CreativeWork):
    jurisdiction: Optional[Any] = None
    legislationApplies: Optional[Any] = None
    legislationChanges: Optional[Any] = None
    legislationConsolidates: Optional[Any] = None
    legislationDate: Optional[Any] = None
    legislationDateVersion: Optional[Any] = None
    legislationIdentifier: Optional[Any] = None
    legislationJurisdiction: Optional[Any] = None
    legislationLegalForce: Optional[Any] = None
    legislationPassedBy: Optional[Any] = None
    legislationResponsible: Optional[Any] = None
    legislationTransposes: Optional[Any] = None
    legislationType: Optional[Any] = None

