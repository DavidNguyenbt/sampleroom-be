from app.models.model import ManpowerCreateData, ManpowerData, ManpowerDataResponse, ManpowerDeleteData, ManpowerInsertAbsentData, ManpowerUpdateData
from app.repositories.manpower_repository import ManpowerRepository


class ManpowerService:
    def __init__(self, repository: ManpowerRepository | None = None):
        self.repository = repository or ManpowerRepository()

    def get_manpower_data(
        self,
        brand: str,
    ) -> ManpowerDataResponse:
        params = (brand,)
        return self.repository.get_manpower_data(params=params)

    def insert_manpower_data(self, manpower: ManpowerCreateData) -> int:
        return self.repository.insert_manpower_data(manpower=manpower)

    def update_manpower(self, manpower: ManpowerUpdateData) -> int:
        return self.repository.update_manpower(manpower=manpower)

    def delete_manpower(self, data: ManpowerDeleteData) -> int:
        return self.repository.delete_manpower(data=data)

    def insert_absent_data(self, data: ManpowerInsertAbsentData) -> int:
        return self.repository.insert_absent_data(data=data)
