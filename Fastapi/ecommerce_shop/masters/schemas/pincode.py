from pydantic import BaseModel , EmailStr ,ConfigDict,Field
from typing import List, Optional
from datetime import datetime
from .base_mixin import BaseSchema


class ResPincodeSchema(BaseSchema):
    name: str = Field(..., pattern=r"^[a-zA-Z0-9\s-]+$") # Flexible for global zips
    city_id: int
    state_id: int
    country_id: int