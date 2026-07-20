from fastapi import APIRouter, Depends, HTTPException
from app.models.model import CreateOperatorData, CreateProductionData, DocnoDataResponse, ManpowerOperatorData, ProductionProgressResponse, ProductionResponse, PatternDataResponse
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

@production_router.get("/production_progress/{customer}/{department}", response_model=list[ProductionProgressResponse])
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

@production_router.get("/operator/{production_id}", response_model=list[ManpowerOperatorData])
def get_operator_data(
    production_id: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.get_operator_data(production_id=production_id)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.delete("/operator/{production_id}/{operator}/{removed_by}", response_model=None)
def remove_operator_data(
    production_id: str,
    operator: str,
    removed_by: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        service.remove_operator_data(production_id=production_id, operator=operator, removed_by=removed_by)
        return None
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.delete("/production/{production_id}/{removed_by}", response_model=None)
def remove_production_data(
    production_id: str,
    removed_by: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        service.remove_production_data(production_id=production_id, removed_by=removed_by)
        return None
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

@production_router.put("/production/{production_id}/{updated_by}/{customer}/{department}", response_model=None)
def update_production_data(
    production_id: str,
    updated_by: str,
    customer: str,
    department: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        service.update_production_data(production_id=production_id, updated_by=updated_by, customer=customer, department=department)
        return None
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
@production_router.get("/production_exists/{docno}/{customer}", response_model=bool)
def check_production_exists(
    docno: str,
    customer: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.check_production_exists(docno=docno, customer=customer)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )  

@production_router.get("/production_progress_exists/{docno}/{department}/{customer}", response_model=bool)
def check_production_progress_exists(
    docno: str,
    department: str,
    customer: str,
    service: ProductionService = Depends(get_production_service),
):
    try:
        return service.check_production_progress_exists(docno=docno, department=department, customer=customer)
    except RuntimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )