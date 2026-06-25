from app.models.model import HomeDataResponse, MasterPlan, Overview, InPattern, InDecoration, InProduction, Completed
from app.repositories.base_repository import BaseRepository


class HomeDataRepository(BaseRepository):

    def get_dashboard(
        self,
        brand: str,
        month: str,
    ) -> HomeDataResponse:

        query = """
        EXEC [api].[SampleRoomQuery] 1,?,?,''
        """

        params = (brand, month)

        results = self.execute_query(query, params)

        if len(results) < 6 or any(not section for section in results[:5]):
            raise RuntimeError("Dashboard query returned incomplete data")

        return HomeDataResponse(
            overview=Overview(**results[0][0]),
            in_pattern=InPattern(**results[1][0]),
            in_decoration=InDecoration(**results[2][0]),
            in_production=InProduction(**results[3][0]),
            completed=Completed(**results[4][0]),
            master_plan=[MasterPlan(**row) for row in results[5]],
        )