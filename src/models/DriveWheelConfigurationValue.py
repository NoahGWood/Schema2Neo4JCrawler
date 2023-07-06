from pydantic import BaseModel
from typing import Optional, Any

class DriveWheelConfigurationValue(BaseModel):
    driveWheelConfiguration: Optional[Any] = None

