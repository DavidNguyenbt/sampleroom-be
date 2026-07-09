from typing import List
from datetime import date, datetime

from pydantic import BaseModel

class Overview(BaseModel):
    total_order: int
    completed: int
    balance: int

class InPattern(BaseModel):
    total_qty: int
    total_style: int

class InDecoration(BaseModel):
    total_qty: int
    total_style: int

class InProduction(BaseModel):
    total_qty: int
    total_style: int

class Completed(BaseModel):
    total_qty: int
    on_time: int
    delay: int

class MasterPlan(BaseModel):
    order_date: date | None = None
    sample_number: str | None = None
    style: str | None = None
    season: str | None = None
    sample_owner: str | None = None
    qty: int | None = None
    status: str | None = None
    smv: float | None = None
    bonding: int | None = None
    printing: int | None = None
    shipment: date | None = None

class HomeDataResponse(BaseModel):
    overview: Overview
    in_pattern: InPattern
    in_decoration: InDecoration
    in_production: InProduction
    completed: Completed
    master_plan: List[MasterPlan]

class ManpowerData(BaseModel):
    RecNo: int
    Customer: str
    Department: str
    Section: str
    EmployeeID: str
    EmployeeName: str
    Position: str
    SysCreatedDate: datetime
    SysLMDate: datetime
    SysLMBy: str

class ManpowerCreateData(BaseModel):
    Customer: str
    Department: str
    Section: str
    EmployeeID: str
    EmployeeName: str
    Position: str
    SysLMBy: str

class EmployeeData(BaseModel):
    ID: str
    Name: str
    Department: str
    Position: str

class ManpowerUpdateData(BaseModel):
    RecNo: int
    Department: str
    Section: str
    Position: str
    SysLMBy: str

class ManpowerDeleteData(BaseModel):
    RecNo: int
    SysLMBy: str

class ManpowerInsertAbsentData(BaseModel):
    EmployeeID: str
    FromDate: date
    ToDate: date
    SysCreatedBy: str

class ManpowerAbsentData(BaseModel):
    RecNo: int
    EmployeeID: str
    FromDate: date
    ToDate: date
    SysCreatedDate: datetime
    SysCreatedBy: str

class ManpowerOperatorData(BaseModel):
    RecNo: int
    ProductionID: str
    Operator: str
    CreatedDate: datetime
    CreatedBy: str

class ManpowerDataResponse(BaseModel):
    manpower: List[ManpowerData]
    absent: List[ManpowerAbsentData]
    operator: List[ManpowerOperatorData]

class PatternDataResponse(BaseModel):
    order_date: date | None = None
    sample_number: str | None = None
    style: str | None = None
    season: str | None = None
    sample_owner: str | None = None
    qty: int | None = None
    pattern: date | None = None

class CreateProductionData(BaseModel):
    customer: str
    department: str
    section: str
    doc_no: str
    user_id: str

class ProductionResponse(BaseModel):
    production_id: str

class ProductionProgressResponse(BaseModel):
    production_id: str
    order_date: date | None = None
    style: str | None = None
    season: str | None = None
    qty: int | None = None
    smv: float | None = None
    starttime: datetime | None = None
    finishtime: datetime | None = None
    duration: float | None = None
    manpower: int | None = None
    downtime: float | None = None

class CreateOperatorData(BaseModel):
    production_id: str
    operator: str
    created_by: str

class DocnoDataResponse(BaseModel):
    doc_no: str
    style: str
    season: str
    qty: int

class OperatorRemoveData(BaseModel):
    production_id: str
    operator: str
    removed_by: str
