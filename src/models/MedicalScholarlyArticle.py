from pydantic import BaseModel
from models.Article import Article

from typing import Optional, Any

class MedicalScholarlyArticle(Article):
    publicationType: Optional[Any] = None

