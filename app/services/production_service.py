from app.repositories.production_repository import ProductionRepository
from app.models.model import CreateProductionData, ProductionProgressResponse, ProductionResponse, PatternDataResponse

class ProductionService:
    def __init__(self, production_repository: ProductionRepository | None = None):
        self.production_repository = production_repository or ProductionRepository()

    def create_production(self, data: CreateProductionData) -> ProductionResponse:
        return self.production_repository.create_production(data)

    def get_pattern_data(self, brand: str, month: str) -> list[PatternDataResponse]:
        return self.production_repository.get_pattern_data(brand, month)

    def get_production_progress(self, customer: str, department: str) -> ProductionProgressResponse:
        return self.production_repository.get_production_progress(customer, department)