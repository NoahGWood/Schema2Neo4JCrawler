from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class InsuranceAgency(LocalBusiness):
    feesAndCommissionsSpecification: Optional[Any] = None

