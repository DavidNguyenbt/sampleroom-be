from fastapi import APIRouter

from app.api.endpoints.homedata import homedata_router
from app.api.endpoints.workforce import workforce_router
from app.api.endpoints.production import production_router    
from app.api.endpoints.dashboard import dashboard_router


api_router = APIRouter()
api_router.include_router(homedata_router)
api_router.include_router(workforce_router)
api_router.include_router(production_router)
api_router.include_router(dashboard_router)
