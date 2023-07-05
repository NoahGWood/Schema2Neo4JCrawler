from pydantic import BaseModel
from models.InvestmentOrDeposit import InvestmentOrDeposit

from typing import Optional, Any

class DepositAccount(InvestmentOrDeposit):
    accountMinimumInflow: Optional[Any] = None
    accountOverdraftLimit: Optional[Any] = None
    bankAccountType: Optional[Any] = None

