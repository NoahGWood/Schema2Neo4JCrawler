from pydantic import BaseModel
from models.FinancialProduct import FinancialProduct

from typing import Optional, Any

class PaymentCard(FinancialProduct):
    cashBack: Optional[Any] = None
    contactlessPayment: Optional[Any] = None
    floorLimit: Optional[Any] = None
    monthlyMinimumRepaymentAmount: Optional[Any] = None

