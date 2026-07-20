from app.repositories.production_repository import ProductionRepository
from app.models.model import CreateProductionData, ProductionProgressResponse, ProductionResponse, PatternDataResponse, ManpowerOperatorData

class ProductionService:
    def __init__(self, production_repository: ProductionRepository | None = None):
        self.production_repository = production_repository or ProductionRepository()

    def create_production(self, data: CreateProductionData) -> ProductionResponse:
        return self.production_repository.create_production(data)

    def get_pattern_data(self, brand: str, month: str) -> list[PatternDataResponse]:
        return self.production_repository.get_pattern_data(brand, month)

    def get_production_progress(self, customer: str, department: str) -> list[ProductionProgressResponse]:
        return self.production_repository.get_production_progress(customer, department)

    def update_pattern_data(self, sample_number: str, receive_date: str) -> int:
        return self.production_repository.update_pattern_data(sample_number, receive_date)

    def get_docno_data(self, doc_no: str):
        return self.production_repository.get_docno_data(doc_no)

    def insert_operator_data(self, production_id: str, operator: str, created_by: str) -> None:
        self.production_repository.insert_operator_data(production_id, operator, created_by)

    def get_operator_data(self, production_id: str) -> list[ManpowerOperatorData]:
        return self.production_repository.get_operator_data(production_id)

    def remove_operator_data(self, production_id: str, operator: str, removed_by: str) -> None:
        self.production_repository.remove_operator_data(production_id, operator, removed_by)

    def remove_production_data(self, production_id: str, removed_by: str) -> None:
        self.production_repository.remove_production_data(production_id, removed_by)

    def update_production_data(self, production_id: str, updated_by: str, customer: str, department: str) -> None:
        self.production_repository.update_production_data(production_id, updated_by, customer, department)

    def check_production_progress_exists(self, docno: str, department: str, customer: str) -> bool:
        return self.production_repository.check_production_progress_exists(docno, department, customer)

    def check_production_exists(self, docno: str, customer: str) -> bool:
        return self.production_repository.check_production_exists(docno, customer)