from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class RepaymentSpecification(Thing):
    downPayment: Optional[Any] = None
    earlyPrepaymentPenalty: Optional[Any] = None
    loanPaymentAmount: Optional[Any] = None
    loanPaymentFrequency: Optional[Any] = None
    numberOfLoanPayments: Optional[Any] = None

