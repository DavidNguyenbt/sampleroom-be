from app.models.model import CreateProductionData, DocnoDataResponse, ManpowerOperatorData, ProductionProgressResponse, ProductionResponse, PatternDataResponse
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

    def get_production_progress(self, customer: str, department: str) -> list[ProductionProgressResponse]:
        query = """
        EXEC [api].[SampleRoomQuery] 7, ?, ?, '', '', ''
        """
        params = (customer, department)
        results = self.execute_query(query=query, params=params)

        if not results or not results[0]:
            raise RuntimeError("No production progress data found")

        return [ProductionProgressResponse(**row) for row in results[0]]

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

    def get_operator_data(self, production_id: str) -> list[ManpowerOperatorData]:
        query = """
        EXEC [api].[SampleRoomQuery] 10, ?, '', '', '', ''
        """
        params = (production_id,)
        results = self.execute_query(query=query, params=params)

        if not results or not results[0]:
            raise RuntimeError("No operator data found")

        return [ManpowerOperatorData(**row) for row in results[0]]

    def remove_operator_data(self, production_id: str, operator: str, removed_by: str) -> None:
        query = """
        EXEC [api].[SampleRoomQuery] 11, ?, ?, ?, '', ''
        """
        params = (production_id, operator, removed_by)
        self.execute_non_query(query=query, params=params)

    def remove_production_data(self, production_id: str, removed_by: str) -> None:
        query = """
        EXEC [api].[SampleRoomQuery] 12, ?, ?, '', '', ''
        """
        params = (production_id, removed_by)
        self.execute_non_query(query=query, params=params)

    def update_production_data(self, production_id: str, updated_by: str, customer: str, department: str) -> None:
        query = """
        EXEC [api].[SampleRoomQuery] 13, ?, ?, ?, ?, ''
        """
        params = (production_id, updated_by, customer, department)
        self.execute_non_query(query=query, params=params)

    def check_production_progress_exists(self, production_id: str) -> bool:
        query = """
        EXEC [api].[SampleRoomQuery] 14, ?, '', '', '', ''
        """
        params = (production_id,)
        results = self.execute_query(query=query, params=params)

        return bool(results and results[0])

    def check_production_exists(self, docno: str) -> bool:
        query = """
        EXEC [api].[SampleRoomQuery] 15, ?, '', '', '', ''
        """
        params = (docno,)
        results = self.execute_query(query=query, params=params)

        return bool(results and results[0])