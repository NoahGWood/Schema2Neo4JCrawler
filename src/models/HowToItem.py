from pydantic import BaseModel
from models.ListItem import ListItem

from typing import Optional, Any

class HowToItem(ListItem):
    requiredQuantity: Optional[Any] = None

