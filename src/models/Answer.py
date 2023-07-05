from pydantic import BaseModel
from models.Comment import Comment

from typing import Optional, Any

class Answer(Comment):
    answerExplanation: Optional[Any] = None

