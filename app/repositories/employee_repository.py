from typing import Any

from app.models.model import EmployeeData
from app.repositories.base_repository import BaseRepository


class EmployeeRepository(BaseRepository):
    def get_employee_data(
        self,
        params: tuple[Any, ...],
    ) -> list[EmployeeData]:
        query = """
        EXEC [api].[SampleRoomQuery] 2,?,'','','',''
        """
        results = self.execute_query(query=query, params=params)

        if not results:
            return []

        return [EmployeeData(**row) for row in results[0]]
