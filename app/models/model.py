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