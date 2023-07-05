from pydantic import BaseModel
from models.TransferAction import TransferAction

from typing import Optional, Any

class BorrowAction(TransferAction):
    lender: Optional[Any] = None

