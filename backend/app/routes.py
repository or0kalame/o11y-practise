from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import crud
import time 

router = APIRouter()

class Package(BaseModel):
    tracking_number: str
    warehouse_number: str
    product_name: str

@router.post("/add_package")
def add_package(pkg: Package):
    data = pkg.dict()
    data["status"] = "formed"
    crud.upsert_package(data)
    return {"message": "Package added"}

@router.get("/get")
def get_package(tracking_number: str):
    result = crud.get_package(tracking_number)
    # time.sleep(1.5)
    if result:
        return dict(result[0])
    raise HTTPException(status_code=404, detail="Package not found")

@router.get("/tracking_numbers")
def list_tracking_numbers():
    return crud.get_all_tracking_numbers()