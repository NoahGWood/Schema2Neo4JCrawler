from pydantic import BaseModel
from models.FinancialProduct import FinancialProduct

from typing import Optional, Any

class LoanOrCredit(FinancialProduct):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    gracePeriod: Optional[Any] = None
    loanRepaymentForm: Optional[Any] = None
    loanTerm: Optional[Any] = None
    loanType: Optional[Any] = None
    recourseLoan: Optional[Any] = None
    renegotiableLoan: Optional[Any] = None
    requiredCollateral: Optional[Any] = None

