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

            metric_fields = (
                "monthinput",
                "monthfinished",
                "todayinput",
                "todayfinished",
            )
            input_vs_finish = []
            for index in range(5):
                if len(results) > index and results[index]:
                    row = results[index][0]
                    metric_data = {
                        field: row.get(field) if row.get(field) is not None else 0
                        for field in metric_fields
                    }
                    input_vs_finish.append(InputvsFinishData(**metric_data))
                else:
                    input_vs_finish.append(
                        InputvsFinishData(
                            monthinput=0,
                            monthfinished=0,
                            todayinput=0,
                            todayfinished=0,
                        )
                    )
            status_rows = results[5] if len(results) > 5 else []

            return DashboardData(
                cutting=input_vs_finish[0],
                embroidery=input_vs_finish[1],
                heattransfer=input_vs_finish[2],
                padprint=input_vs_finish[3],
                sewing=input_vs_finish[4],
                statusdata=[ProductionStatusData(**row) for row in status_rows],
            )