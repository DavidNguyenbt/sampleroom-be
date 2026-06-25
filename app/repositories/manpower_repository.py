from typing import Any

from app.models.model import ManpowerCreateData, ManpowerData
from app.repositories.base_repository import BaseRepository


class ManpowerRepository(BaseRepository):
    def get_manpower_data(
        self,
        params: tuple[Any, ...],
    ) -> list[ManpowerData]:
        query = """
        EXEC [api].[SampleRoomQuery] 3,?,'',''
        """
        results = self.execute_query(query=query, params=params)

        if not results:
            return []

        return [ManpowerData(**row) for row in results[0]]

    def insert_manpower_data(self, manpower: ManpowerCreateData) -> int:
        query = """
        INSERT INTO [dbo].[SampleRoomManpower]
        (
            [Customer],
            [Department],
            [Section],
            [EmployeeID],
            [EmployeeName],
            [Position],
            [SysCreatedDate],
            [SysLMDate],
            [SysLMBy]
        )
        VALUES (?, ?, ?, ?, ?, ?, GETDATE(), GETDATE(), ?)
        """

        params = (
            manpower.Customer,
            manpower.Department,
            manpower.Section,
            manpower.EmployeeID,
            manpower.EmployeeName,
            manpower.Position,
            manpower.SysLMBy,
        )
        return self.execute_non_query(query=query, params=params)
