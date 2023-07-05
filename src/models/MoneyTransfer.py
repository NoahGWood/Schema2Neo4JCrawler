from pydantic import BaseModel
from models.TransferAction import TransferAction

from typing import Optional, Any

class MoneyTransfer(TransferAction):
    amount: Optional[Any] = None
    beneficiaryBank: Optional[Any] = None

