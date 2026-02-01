from sqlalchemy import Column,Boolean,String,Integer,Float,ForeignKey,Enum
from ecommerce_shop.database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from Fastapi.ecommerce_shop.masters.models import BaseMixin

class ResUsers(Base,BaseMixin):
    __tablename__ = "res_users"

    email = Column(String, index=True, unique=True, nullable=False)
    password= Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    partner_profile = relationship("ResPartner", back_populates="user", uselist=False)


class ResPartner(Base, BaseMixin):
    __tablename__ = "res_partner"

    
    #Link to User
    user_id = Column(Integer, ForeignKey("res_users.id", ondelete="CASCADE"), nullable=False)
    username = Column(String, nullable=False)
    
    # Address Blocks (Relational)
    street = Column(String, nullable=True)  # House No, Building
    street2 = Column(String, nullable=True) # Area, Colony (Renamed street1 to street2 to match Odoo)
    
    # Instead of Strings, use IDs for data integrity
    city_id = Column(Integer, ForeignKey("res_city.id"), nullable=True) # If you created ResCity
    state_id = Column(Integer, ForeignKey("res_country_state.id"), nullable=True)
    country_id = Column(Integer, ForeignKey("res_country.id"), nullable=True)
    pincode_id = Column(Integer, ForeignKey("res_pincode.id"), nullable=True)

    # Relationships (Odoo Many2one links)
    user = relationship("ResUsers", back_populates="partner_profile")
    state = relationship("ResCountryState")
    country = relationship("ResCountry")
    pincode = relationship("ResPincode")