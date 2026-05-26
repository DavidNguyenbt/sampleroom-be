from app.core.ResponseApi import ResponseAPI
from fastapi import APIRouter, HTTPException
from app.respositories.respository import ParamConfigRepository
from app.models.model import HomeDataResponse

homedata_router = APIRouter()

@homedata_router.get("/home-data/{type}/{brand}/{month}", response_model=HomeDataResponse)
def get_home_data(type: int, brand: str, month: str):
    repo = ParamConfigRepository()
    try:
        return repo.get_dashboard(type=type, brand=brand, month=month)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )