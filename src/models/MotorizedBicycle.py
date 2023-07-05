from pydantic import BaseModel
from models.Product import Product

from typing import Optional, Any

class MotorizedBicycle(Product):
    accelerationTime: Optional[Any] = None
    bodyType: Optional[Any] = None
    callSign: Optional[Any] = None
    cargoVolume: Optional[Any] = None
    dateVehicleFirstRegistered: Optional[Any] = None
    driveWheelConfiguration: Optional[Any] = None
    emissionsCO2: Optional[Any] = None
    fuelCapacity: Optional[Any] = None
    fuelConsumption: Optional[Any] = None
    fuelEfficiency: Optional[Any] = None
    fuelType: Optional[Any] = None
    knownVehicleDamages: Optional[Any] = None
    meetsEmissionStandard: Optional[Any] = None
    mileageFromOdometer: Optional[Any] = None
    modelDate: Optional[Any] = None
    numberOfAirbags: Optional[Any] = None
    numberOfAxles: Optional[Any] = None
    numberOfDoors: Optional[Any] = None
    numberOfForwardGears: Optional[Any] = None
    numberOfPreviousOwners: Optional[Any] = None
    payload: Optional[Any] = None
    productionDate: Optional[Any] = None
    purchaseDate: Optional[Any] = None
    seatingCapacity: Optional[Any] = None
    speed: Optional[Any] = None
    steeringPosition: Optional[Any] = None
    tongueWeight: Optional[Any] = None
    trailerWeight: Optional[Any] = None
    vehicleConfiguration: Optional[Any] = None
    vehicleEngine: Optional[Any] = None
    vehicleIdentificationNumber: Optional[Any] = None
    vehicleInteriorColor: Optional[Any] = None
    vehicleInteriorType: Optional[Any] = None
    vehicleModelDate: Optional[Any] = None
    vehicleSeatingCapacity: Optional[Any] = None
    vehicleSpecialUsage: Optional[Any] = None
    vehicleTransmission: Optional[Any] = None
    weightTotal: Optional[Any] = None
    wheelbase: Optional[Any] = None

