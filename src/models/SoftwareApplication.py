from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class SoftwareApplication(CreativeWork):
    applicationCategory: Optional[Any] = None
    applicationSubCategory: Optional[Any] = None
    applicationSuite: Optional[Any] = None
    availableOnDevice: Optional[Any] = None
    countriesNotSupported: Optional[Any] = None
    countriesSupported: Optional[Any] = None
    downloadUrl: Optional[Any] = None
    featureList: Optional[Any] = None
    fileSize: Optional[Any] = None
    installUrl: Optional[Any] = None
    memoryRequirements: Optional[Any] = None
    operatingSystem: Optional[Any] = None
    permissions: Optional[Any] = None
    processorRequirements: Optional[Any] = None
    releaseNotes: Optional[Any] = None
    screenshot: Optional[Any] = None
    softwareAddOn: Optional[Any] = None
    softwareHelp: Optional[Any] = None
    softwareRequirements: Optional[Any] = None
    softwareVersion: Optional[Any] = None
    storageRequirements: Optional[Any] = None
    supportingData: Optional[Any] = None

