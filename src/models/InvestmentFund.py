from pydantic import BaseModel
from models.FinancialProduct import FinancialProduct

from typing import Optional, Any

class InvestmentFund(FinancialProduct):
    amount: Optional[Any] = None

