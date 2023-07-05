from pydantic import BaseModel
from models.TransferAction import TransferAction

from typing import Optional, Any

class SendAction(TransferAction):
    deliveryMethod: Optional[Any] = None
    recipient: Optional[Any] = None

