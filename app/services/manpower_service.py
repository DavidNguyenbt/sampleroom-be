from app.models.model import ManpowerCreateData, ManpowerData
from app.repositories.manpower_repository import ManpowerRepository


class ManpowerService:
    def __init__(self, repository: ManpowerRepository | None = None):
        self.repository = repository or ManpowerRepository()

    def get_manpower_data(
        self,
        brand: str,
    ) -> list[ManpowerData]:
        params = (brand,)
        return self.repository.get_manpower_data(params=params)

    def insert_manpower_data(self, manpower: ManpowerCreateData) -> int:
        return self.repository.insert_manpower_data(manpower=manpower)
