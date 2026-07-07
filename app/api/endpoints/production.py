from fastapi import APIRouter, Depends, HTTPException
from app.models.model import CreateOperatorData, CreateProductionData, DocnoDataResponse, ProductionProgressResponse, ProductionResponse, PatternDataResponse
from app.services.production_service import ProductionService

production_router = APIRouter()


def get_production_service() -> ProductionService:
    return ProductionService()


@production_router.get("/production/{customer}/{docno}/{department}/{user_id}/{section}", response_model=ProductionResponse)
def create_production(
    customer: str,
    docno: str,
    department: str,
    user_id: str,
    section: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.create_production(CreateProductionData(customer=customer, doc_no=docno, department=department, user_id=user_id, section=section))
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.get("/pattern/{brand}/{month}", response_model=list[PatternDataResponse])
def get_pattern_data(
    brand: str,
    month: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.get_pattern_data(brand=brand, month=month)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.get("/production_progress/{customer}/{department}", response_model=ProductionProgressResponse)
def get_production_progress(
    customer: str,
    department: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.get_production_progress(customer=customer, department=department)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.put("/pattern/{sample_number}/{receive_date}", response_model=int)
def update_pattern_data(
    sample_number: str,
    receive_date: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.update_pattern_data(sample_number=sample_number, receive_date=receive_date)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.get("/docno/{doc_no}", response_model=DocnoDataResponse)
def get_docno_data(
    doc_no: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.get_docno_data(doc_no=doc_no)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.post("/operator", response_model=CreateOperatorData)
def insert_operator_data(
    production_id: str,
    operator: str,
    created_by: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        service.insert_operator_data(production_id=production_id, operator=operator, created_by=created_by)
        return CreateOperatorData(production_id=production_id, operator=operator, created_by=created_by)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )