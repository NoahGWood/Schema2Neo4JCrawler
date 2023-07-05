from pydantic import BaseModel
from models.Product import Product

from typing import Optional, Any

class ProductModel(Product):
    isVariantOf: Optional[Any] = None
    predecessorOf: Optional[Any] = None
    successorOf: Optional[Any] = None

