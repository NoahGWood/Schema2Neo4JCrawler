from pydantic import BaseModel
from models.Product import Product

from typing import Optional, Any

class SomeProducts(Product):
    inventoryLevel: Optional[Any] = None

