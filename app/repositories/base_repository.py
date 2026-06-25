from typing import Any

import pyodbc

from app.core.config import settings


class BaseRepository:
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
            raise RuntimeError(f"Database connection error: {e}") from e

    def execute_query(self, query: str, params: tuple[Any, ...] | None = None):
        """Execute query and return all result sets."""
        results = []

        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    if params:
                        cursor.execute(query, params)
                    else:
                        cursor.execute(query)

                    while True:
                        if cursor.description is not None:
                            columns = [column[0] for column in cursor.description]
                            rows = cursor.fetchall()
                            results.append([dict(zip(columns, row)) for row in rows])

                        if not cursor.nextset():
                            break

            return results
        except Exception as e:
            raise RuntimeError(f"Database query error: {e}") from e

    def execute_non_query(self, query: str, params: tuple[Any, ...] | None = None) -> int:
        """Execute INSERT/UPDATE/DELETE statements and return affected row count."""
        try:
            with self.connect() as conn:
                with conn.cursor() as cursor:
                    if params:
                        cursor.execute(query, params)
                    else:
                        cursor.execute(query)

                    affected_rows = cursor.rowcount
                conn.commit()

            return affected_rows
        except Exception as e:
            raise RuntimeError(f"Database command error: {e}") from e
