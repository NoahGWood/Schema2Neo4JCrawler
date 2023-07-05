from pydantic import BaseModel
from models.TransferAction import TransferAction

from typing import Optional, Any

class LendAction(TransferAction):
    borrower: Optional[Any] = None

