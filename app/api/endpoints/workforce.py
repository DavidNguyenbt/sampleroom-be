from fastapi import APIRouter, Depends, HTTPException

from app.models.model import EmployeeData, ManpowerCreateData, ManpowerData, ManpowerDeleteData, ManpowerInsertAbsentData, ManpowerUpdateData
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

@workforce_router.put("/manpower", response_model=dict[str, int])
def update_manpower_data(
    manpower: ManpowerUpdateData,
    service: ManpowerService = Depends(get_manpower_service),
):
    try:
        affected_rows = service.update_manpower(manpower=manpower)
        return {"updated_rows": affected_rows}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@workforce_router.delete("/manpower", response_model=dict[str, int])
def delete_manpower_data(
    data: ManpowerDeleteData,
    service: ManpowerService = Depends(get_manpower_service),
):
    try:
        affected_rows = service.delete_manpower(data=data)
        return {"deleted_rows": affected_rows}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@workforce_router.post("/manpower/absent", response_model=dict[str, int])
def insert_absent_data(
    data: ManpowerInsertAbsentData,
    service: ManpowerService = Depends(get_manpower_service),
):
    try:
        affected_rows = service.insert_absent_data(data=data)
        return {"inserted_rows": affected_rows}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
