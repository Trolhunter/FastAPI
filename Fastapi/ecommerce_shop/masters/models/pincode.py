from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ecommerce_shop.database import Base
from ecommerce_shop.masters.models.BaseMixin import BaseMixin

class ResPincode(Base, BaseMixin):
    __tablename__ = "res_pincode"
    
    # The Pincode/Zip string (e.g., "110001" or "90210")
    # We use String because some countries have alphanumeric zips (e.g., UK/Canada)
    name = Column(String(10), index=True, nullable=False)
    
    city_id = Column(Integer, ForeignKey("res_city.id", ondelete="CASCADE"), nullable=False)

    # Many2one: Multiple pincodes belong to one state
    state_id = Column(Integer, ForeignKey("res_country_state.id", ondelete="CASCADE"), nullable=False)
    
    # Many2one: Optional - direct link to country for faster queries
    country_id = Column(Integer, ForeignKey("res_country.id", ondelete="CASCADE"), nullable=False)

    # Relationships (The One2many handshake)
    city = relationship("ResCity", back_populates="pincode_ids")
    state = relationship("ResCountryState", back_populates="pincode_ids")
    country = relationship("ResCountry") 
    
    
    # Advanced: Area/City name associated with this pincode
    district = Column(String, nullable=True)