from app.repositories.dashboard_repository import DashboardRepository
from app.models.model import DashboardData

class DashboardService:
    def __init__(self, repository: DashboardRepository):
        self.repository = repository

    def get_dashboard_data(self, brand: str, month: str) -> DashboardData:
        return self.repository.get_dashboard_data(brand=brand, month=month)