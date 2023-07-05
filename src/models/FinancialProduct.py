from pydantic import BaseModel
from models.Service import Service

from typing import Optional, Any

class FinancialProduct(Service):
    annualPercentageRate: Optional[Any] = None
    feesAndCommissionsSpecification: Optional[Any] = None
    interestRate: Optional[Any] = None

