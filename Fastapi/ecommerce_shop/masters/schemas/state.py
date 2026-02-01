from pydantic import BaseModel , EmailStr ,ConfigDict,Field
from typing import List, Optional
from datetime import datetime
from .base_mixin import BaseSchema

class ResCountryStateSchema(BaseSchema):
    name: str = Field(..., min_length=2, max_length=100)
    country_id: int

class ResCitySchema(BaseSchema):
    name: str = Field(..., min_length=2, max_length=100)
    state_id: int

