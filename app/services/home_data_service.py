from app.models.model import HomeDataResponse
from app.repositories.home_data_repository import HomeDataRepository


class HomeDataService:
    def __init__(self, repository: HomeDataRepository | None = None):
        self.repository = repository or HomeDataRepository()

    def get_home_data(self, brand: str, month: str) -> HomeDataResponse:
        return self.repository.get_dashboard(brand=brand, month=month)
