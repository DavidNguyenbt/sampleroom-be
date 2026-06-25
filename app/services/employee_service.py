from app.models.model import EmployeeData
from app.repositories.employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self, repository: EmployeeRepository | None = None):
        self.repository = repository or EmployeeRepository()

    def get_employee_data(
        self,
        id: str,
    ) -> list[EmployeeData]:
        params = (id,)
        return self.repository.get_employee_data(params=params)
