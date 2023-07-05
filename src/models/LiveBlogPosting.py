from pydantic import BaseModel
from models.SocialMediaPosting import SocialMediaPosting

from typing import Optional, Any

class LiveBlogPosting(SocialMediaPosting):
    coverageEndTime: Optional[Any] = None
    coverageStartTime: Optional[Any] = None
    liveBlogUpdate: Optional[Any] = None

