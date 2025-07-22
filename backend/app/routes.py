from fastapi import APIRouter, HTTPException
from .schemas import PackageCreate, PackageRead
from .crud import create_package, get_package_by_tracking

router = APIRouter()

@router.post("/add_package", response_model=PackageRead)
def add_package(package: PackageCreate):
    return create_package(package)

@router.get("/get", response_model=PackageRead)
def get_package(tracking_number: str):
    result = get_package_by_tracking(tracking_number)
    if not result:
        raise HTTPException(status_code=404, detail="Package not found")
    return PackageRead(**result)
