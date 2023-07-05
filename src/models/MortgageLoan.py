from pydantic import BaseModel
from models.LoanOrCredit import LoanOrCredit

from typing import Optional, Any

class MortgageLoan(LoanOrCredit):
    domiciledMortgage: Optional[Any] = None
    loanMortgageMandateAmount: Optional[Any] = None

