from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class EmailMessage(CreativeWork):
    bccRecipient: Optional[Any] = None
    ccRecipient: Optional[Any] = None
    dateRead: Optional[Any] = None
    dateReceived: Optional[Any] = None
    dateSent: Optional[Any] = None
    messageAttachment: Optional[Any] = None
    recipient: Optional[Any] = None
    sender: Optional[Any] = None
    toRecipient: Optional[Any] = None

