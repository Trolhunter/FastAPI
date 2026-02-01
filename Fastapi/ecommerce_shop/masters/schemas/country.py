from pydantic import BaseModel , EmailStr ,ConfigDict,Field
from typing import List, Optional
from datetime import datetime
from .base_mixin import BaseSchema

class ResCountrySchema(BaseSchema):
    name: str = Field(..., min_length=2, max_length=100)
    country_code: str = Field(..., min_length=2, max_length=3) # e.g., "IN"