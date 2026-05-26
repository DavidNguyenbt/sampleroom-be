from typing import List
from app.core.ResponseApi import ResponseAPI
from app.models.model import HomeDataResponse, MasterPlan, Overview, InPattern, InDecoration, InProduction, Completed
from app.core.config import settings
import pyodbc
from fastapi import HTTPException

class ParamConfigRepository:
    def __init__(self):
        self.connection_string = (
            f"DRIVER={{{settings.DB_DRIVER}}};"
            f"SERVER={settings.DB_SERVER};"
            f"DATABASE={settings.DB_NAME};"
            f"UID={settings.DB_USER};"
            f"PWD={settings.DB_PASSWORD};"
            f"Encrypt={settings.DB_ENCRYPT};"
            f"TrustServerCertificate={settings.DB_TRUST_SERVER_CERTIFICATE};"
        )
    def connect(self):
        try:
            return pyodbc.connect(self.connection_string)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Database connection error: {e}")

    def execute_query(self, query: str, params=None):
        """Execute query and return all result sets"""

        results = []

        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:

                    if params:
                        cursor.execute(query, params)
                    else:
                        cursor.execute(query)

                    while True:

                        # Check if current result set has columns
                        if cursor.description is not None:

                            columns = [column[0] for column in cursor.description]

                            rows = cursor.fetchall()

                            result = [
                                dict(zip(columns, row))
                                for row in rows
                            ]

                            results.append(result)

                        # Move next result set
                        if not cursor.nextset():
                            break

            return results

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
        
        
    def get_dashboard(
        self,
        type: int,
        brand: str,
        month: str
    ) -> HomeDataResponse:

        query = """
        EXEC [api].[SampleRoomQuery] ?,?,?,''
        """

        params = (
            type,
            brand,
            month
        )

        results = self.execute_query(query, params)

        return HomeDataResponse(

            overview=Overview(
                **results[0][0]
            ),

            in_pattern=InPattern(
                **results[1][0]
            ),

            in_decoration=InDecoration(
                **results[2][0]
            ),

            in_production=InProduction(
                **results[3][0]
            ),

            completed=Completed(
                **results[4][0]
            ),

            master_plan=[
                MasterPlan(**row)
                for row in results[5]
            ]
        )