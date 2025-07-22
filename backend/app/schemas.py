from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    formed = "formed"
    in_transit = "transit"
    delivered = "delivered"

class PackageCreate(BaseModel):
    tracking_number: str
    status: StatusEnum
    warehouse_number: str
    product_name: str
    pickup_address: str

class PackageRead(PackageCreate):
    pass
