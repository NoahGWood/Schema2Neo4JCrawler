from pydantic import BaseModel
from models.FinancialProduct import FinancialProduct

from typing import Optional, Any

class BankAccount(FinancialProduct):
    accountMinimumInflow: Optional[Any] = None
    accountOverdraftLimit: Optional[Any] = None
    bankAccountType: Optional[Any] = None

