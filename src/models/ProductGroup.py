from pydantic import BaseModel
from models.Product import Product

from typing import Optional, Any

class ProductGroup(Product):
    hasVariant: Optional[Any] = None
    productGroupID: Optional[Any] = None
    variesBy: Optional[Any] = None

