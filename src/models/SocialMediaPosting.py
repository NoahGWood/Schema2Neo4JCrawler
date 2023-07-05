from pydantic import BaseModel
from models.Article import Article

from typing import Optional, Any

class SocialMediaPosting(Article):
    sharedContent: Optional[Any] = None

