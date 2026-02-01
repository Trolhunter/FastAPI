from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional, List

# --- BASE MIXIN FOR SCHEMAS ---
class BaseSchema(BaseModel):
    is_active: bool = True
    # Enables Pydantic to read SQLAlchemy models directly
    model_config = ConfigDict(from_attributes=True)