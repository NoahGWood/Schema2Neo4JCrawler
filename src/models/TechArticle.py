from pydantic import BaseModel
from models.Article import Article

from typing import Optional, Any

class TechArticle(Article):
    dependencies: Optional[Any] = None
    proficiencyLevel: Optional[Any] = None

