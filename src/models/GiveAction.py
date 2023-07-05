from pydantic import BaseModel
from models.TransferAction import TransferAction

from typing import Optional, Any

class GiveAction(TransferAction):
    recipient: Optional[Any] = None

