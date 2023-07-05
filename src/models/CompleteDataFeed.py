from pydantic import BaseModel
from models.Dataset import Dataset

from typing import Optional, Any

class CompleteDataFeed(Dataset):
    dataFeedElement: Optional[Any] = None

