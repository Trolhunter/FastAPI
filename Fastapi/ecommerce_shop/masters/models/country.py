from sqlalchemy import Column,String,Integer,Boolean
from ecommerce_shop.database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from ecommerce_shop.masters.models.BaseMixin import BaseMixin

class ResCountry(Base,BaseMixin):
    __tablename__ = "res_country"

    name = Column(String, nullable=False)
    country_code = Column(String, nullable=False, unique=True)
    state_ids = relationship("ResCountryState", back_populates="country", cascade="all, delete-orphan")
