from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class AccountingService(LocalBusiness):
    feesAndCommissionsSpecification: Optional[Any] = None

