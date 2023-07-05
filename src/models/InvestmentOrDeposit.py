from pydantic import BaseModel
from models.FinancialProduct import FinancialProduct

from typing import Optional, Any

class InvestmentOrDeposit(FinancialProduct):
    amount: Optional[Any] = None

