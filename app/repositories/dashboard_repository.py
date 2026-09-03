from app.models.model import DashboardData, InputvsFinishData, ProductionStatusData
from app.repositories.base_repository import BaseRepository

class DashboardRepository(BaseRepository):
    def get_dashboard_data(
            self,
            brand: str,
        month: str,
        ) -> DashboardData:
            query = """
            EXEC [api].[SampleRoomQuery] 16,?,?,'','',''
            """
            params = (brand, month)
            results = self.execute_query(query=query, params=params)
    
            if not results:
                return DashboardData(
                    cutting=InputvsFinishData(monthinput=0, monthfinished=0, todayinput=0, todayfinished=0),
                    embroidery=InputvsFinishData(monthinput=0, monthfinished=0, todayinput=0, todayfinished=0),
                    heattransfer=InputvsFinishData(monthinput=0, monthfinished=0, todayinput=0, todayfinished=0),
                    padprint=InputvsFinishData(monthinput=0, monthfinished=0, todayinput=0, todayfinished=0),
                    sewing=InputvsFinishData(monthinput=0, monthfinished=0, todayinput=0, todayfinished=0),
                    statusdata=[ProductionStatusData()]
                )

            return DashboardData(
                cutting=InputvsFinishData(**results[0][0]),
                embroidery=InputvsFinishData(**results[1][0]),
                heattransfer=InputvsFinishData(**results[2][0]),
                padprint=InputvsFinishData(**results[3][0]),
                sewing=InputvsFinishData(**results[4][0]),
                statusdata=[ProductionStatusData(**r) for r in results[5]]
            )