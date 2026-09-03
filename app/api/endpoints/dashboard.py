from fastapi import APIRouter, Depends, HTTPException
from app.services.dashboard_service import DashboardService
from app.repositories.dashboard_repository import DashboardRepository
from app.models.model import DashboardData

dashboard_router = APIRouter()

def get_dashboard_service() -> DashboardService:
    return DashboardService(repository=DashboardRepository())

@dashboard_router.get("/dashboard/{brand}/{month}", response_model=DashboardData)
def get_dashboard_data(brand: str, month: str, service: DashboardService = Depends(get_dashboard_service)) -> DashboardData:
    try:
        return service.get_dashboard_data(brand=brand, month=month)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))