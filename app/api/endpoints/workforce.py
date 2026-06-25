from fastapi import APIRouter, Depends, HTTPException

from app.models.model import EmployeeData, ManpowerCreateData, ManpowerData
from app.services.employee_service import EmployeeService
from app.services.manpower_service import ManpowerService


workforce_router = APIRouter()


def get_manpower_service() -> ManpowerService:
    return ManpowerService()


def get_employee_service() -> EmployeeService:
    return EmployeeService()


@workforce_router.get(
    "/manpower/{brand}",
    response_model=list[ManpowerData],
)
def get_manpower_data(
    brand: str,
    service: ManpowerService = Depends(get_manpower_service),
):
    try:
        return service.get_manpower_data(
            brand=brand,
        )
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@workforce_router.post("/manpower", response_model=dict[str, int])
def create_manpower_data(
    manpower: ManpowerCreateData,
    service: ManpowerService = Depends(get_manpower_service),
):
    try:
        affected_rows = service.insert_manpower_data(manpower=manpower)
        return {"inserted_rows": affected_rows}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))


@workforce_router.get(
    "/employee/{id}",
    response_model=list[EmployeeData],
)
def get_employee_data(
    id: str,
    service: EmployeeService = Depends(get_employee_service),
):
    try:
        return service.get_employee_data(id=id)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
