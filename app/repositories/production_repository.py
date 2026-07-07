from app.models.model import CreateProductionData, DocnoDataResponse, ProductionProgressResponse, ProductionResponse, PatternDataResponse
from app.repositories.base_repository import BaseRepository

class ProductionRepository(BaseRepository):
    def create_production(self, data: CreateProductionData) -> ProductionResponse:
        query = """
        EXEC [api].[SampleRoomQuery] 5, ?, ?, ?, ?, ?
        """
        params = (
            data.customer,
            data.doc_no,
            data.department,
            data.user_id,
            data.section,
        )
        results = self.execute_query(query=query, params=params)

        if not results or not results[0]:
            raise RuntimeError("Failed to create production record")

        return ProductionResponse(**results[0][0])

    def get_pattern_data(self, brand: str, month: str) -> list[PatternDataResponse]:
        query = """
        EXEC [api].[SampleRoomQuery] 6, ?, ?, '', '', ''
        """
        params = (brand, month)
        results = self.execute_query(query=query, params=params)

        if not results or not results[0]:
            raise RuntimeError("No pattern data found")

        return [PatternDataResponse(**row) for row in results[0]]

    def get_production_progress(self, customer: str, department: str) -> ProductionProgressResponse:
        query = """
        EXEC [api].[SampleRoomQuery] 7, ?, ?, '', '', ''
        """
        params = (customer, department)
        results = self.execute_query(query=query, params=params)

        if not results or not results[0]:
            raise RuntimeError("No production progress data found")

        return ProductionProgressResponse(**results[0][0])

    def update_pattern_data(self, sample_number: str, receive_date: str) -> int:
        query = """
        UPDATE [dbo].[smomstr2]
        SET
            [PatternReturn] =
        WHERE [DocNo] = ?
        """
        params = (
            receive_date,
            sample_number,
        )
        return self.execute_non_query(query=query, params=params)  

    def get_docno_data(self, doc_no: str) -> DocnoDataResponse:
        query = """
        EXEC [api].[SampleRoomQuery] 8, ?, '', '', '', ''
        """
        params = (doc_no,)
        results = self.execute_query(query=query, params=params)

        if not results or not results[0]:
            raise RuntimeError("No docno data found")

        return DocnoDataResponse(**results[0][0])

    def insert_operator_data(self, production_id: str, operator: str, created_by: str) -> None:
        query = """
        EXEC [api].[SampleRoomQuery] 9, ?, ?, ?, '', ''
        """
        params = (production_id, operator, created_by)
        self.execute_non_query(query=query, params=params)