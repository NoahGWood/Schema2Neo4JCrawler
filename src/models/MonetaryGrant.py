from pydantic import BaseModel
from models.Grant import Grant

from typing import Optional, Any

class MonetaryGrant(Grant):
    amount: Optional[Any] = None
    funder: Optional[Any] = None

