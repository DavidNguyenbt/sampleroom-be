from fastapi import APIRouter, Depends, HTTPException
from app.models.model import HomeDataResponse
from app.services.home_data_service import HomeDataService

homedata_router = APIRouter()


def get_home_data_service() -> HomeDataService:
    return HomeDataService()


@homedata_router.get("/home-data/{brand}/{month}", response_model=HomeDataResponse)
def get_home_data(
    brand: str,
    month: str,
    service: HomeDataService = Depends(get_home_data_service),
):
    try:
        return service.get_home_data(brand=brand, month=month)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )