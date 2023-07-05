from pydantic import BaseModel
from models.ListItem import ListItem

from typing import Optional, Any

class HowToTool(ListItem):
    requiredQuantity: Optional[Any] = None

