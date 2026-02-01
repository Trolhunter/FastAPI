from pydantic import BaseModel , EmailStr ,ConfigDict,Field
from typing import List, Optional
from datetime import datetime
from ecommerce_shop.masters.schemas.base_mixin import BaseSchema


class UserCreate(BaseSchema):
    email: EmailStr
    name: str = Field(...,title="Name", min_length=2)
    password: str = Field(..., min_length=8)


class UserOut(BaseSchema):
    """Schema for Profile Display: Hides Password"""
    email: EmailStr = Field
    name: str = Field(...,title="Name",min_length=2,max_length=20)
    create_date: datetime
    model_config = ConfigDict(from_attributes=True)


class ResPartnerSchema(BaseSchema):
    """The Customer Profile Schema"""
    username: str = Field(...,title="Name",min_length=2,max_length=20)
    user_id: int
    # Address links
    street: Optional[str] = None
    street2: Optional[str] = None
    city_id: Optional[int] = None
    state_id: Optional[int] = None
    pincode_id: Optional[int] = None
    country_id: Optional[int] = None