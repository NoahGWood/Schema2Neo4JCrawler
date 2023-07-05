from pydantic import BaseModel
from models.TransferAction import TransferAction

from typing import Optional, Any

class ReceiveAction(TransferAction):
    deliveryMethod: Optional[Any] = None
    sender: Optional[Any] = None

