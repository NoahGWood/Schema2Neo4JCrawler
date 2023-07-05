from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class CDCPMDRecord(Thing):
    cvdCollectionDate: Optional[Any] = None
    cvdFacilityCounty: Optional[Any] = None
    cvdFacilityId: Optional[Any] = None
    cvdNumBeds: Optional[Any] = None
    cvdNumBedsOcc: Optional[Any] = None
    cvdNumC19Died: Optional[Any] = None
    cvdNumC19HOPats: Optional[Any] = None
    cvdNumC19HospPats: Optional[Any] = None
    cvdNumC19MechVentPats: Optional[Any] = None
    cvdNumC19OFMechVentPats: Optional[Any] = None
    cvdNumC19OverflowPats: Optional[Any] = None
    cvdNumICUBeds: Optional[Any] = None
    cvdNumICUBedsOcc: Optional[Any] = None
    cvdNumTotBeds: Optional[Any] = None
    cvdNumVent: Optional[Any] = None
    cvdNumVentUse: Optional[Any] = None
    datePosted: Optional[Any] = None

