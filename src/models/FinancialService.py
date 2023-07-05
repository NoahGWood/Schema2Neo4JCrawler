from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class FinancialService(LocalBusiness):
    feesAndCommissionsSpecification: Optional[Any] = None

