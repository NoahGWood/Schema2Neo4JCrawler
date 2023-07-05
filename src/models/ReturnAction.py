from pydantic import BaseModel
from models.TransferAction import TransferAction

from typing import Optional, Any

class ReturnAction(TransferAction):
    recipient: Optional[Any] = None

