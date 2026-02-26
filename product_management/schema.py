from pydantic import BaseModel,ConfigDict
from typing import Optional, List,Dict

class ProductTemplateBase(BaseModel):
    name: str
    description: Optional[str] = None
    company_id: int
    location_id: int
    on_hand_qty: int = 0
    price: float = 0.0

class ProductCreate(ProductTemplateBase):
    pass

class ProductUpdate(ProductTemplateBase):
    id: int

class ProductDelete(BaseModel):
    id:int

class ProductRead(ProductTemplateBase):
    id:int
    warehouse_id: int
    is_active: bool
    model_config = ConfigDict(from_attributes=True)

class LocationBase(BaseModel):
    name: str
    description: Optional[str] = None
    company_id: int

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    id: int

class LocationDelete(BaseModel):
    id:int

class LocationRead(LocationBase):
    id:int
    products:List[ProductRead] = []
    model_config = ConfigDict(from_attributes=True)


class WarehouseBase(BaseModel):
    name: str
    description: Optional[str] = None
    company_id: int

class WarehouseCreate(WarehouseBase):
    pass

class WarehouseUpdate(WarehouseBase):
    id: int

class WarehouseDelete(BaseModel):
    id:int

class WarehouseRead(WarehouseBase):
    id:int
    locations:List[LocationRead] = []
    model_config = ConfigDict(from_attributes=True)

class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None

class CompanyRead(CompanyBase):
    id: int
    warehouses: List[WarehouseRead] = []
    model_config = ConfigDict(from_attributes=True)



