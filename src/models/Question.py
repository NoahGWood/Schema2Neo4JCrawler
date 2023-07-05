from pydantic import BaseModel
from models.Comment import Comment

from typing import Optional, Any

class Question(Comment):
    acceptedAnswer: Optional[Any] = None
    answerCount: Optional[Any] = None
    eduQuestionType: Optional[Any] = None
    suggestedAnswer: Optional[Any] = None

