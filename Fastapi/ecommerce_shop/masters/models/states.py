from sqlalchemy import Column,Boolean,String,Integer,Float,ForeignKey,Enum
from ecommerce_shop.database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .country import ResCountry
from ecommerce_shop.masters.models.BaseMixin import BaseMixin

class ResCity(Base, BaseMixin):
    __tablename__ = "res_city"
    
    name = Column(String, nullable=False, index=True)
    
    # Many2one: Multiple cities belong to one state (Odoo style)
    state_id = Column(Integer, ForeignKey("res_country_state.id", ondelete="CASCADE"), nullable=False)
    
    # Relationships
    state = relationship("ResCountryState", back_populates="city_ids")
    
    # One2many: A city has many pincodes
    pincode_ids = relationship("ResPincode", back_populates="city")


class ResCountryState(Base,BaseMixin):
    __tablename__ = "res_country_state"

    name = Column(String, nullable=False)
    country_id = Column(Integer,ForeignKey("res_country.id",ondelete="CASCADE"),nullable=False)
    country = relationship("ResCountry", back_populates="state_ids")
    pincode_ids = relationship("ResPincode", back_populates="state", cascade="all, delete-orphan")
    city_ids = relationship("ResCity", back_populates="state", cascade="all, delete-orphan")