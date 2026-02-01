from sqlalchemy import Column, Boolean, TIMESTAMP, text,Integer
from sqlalchemy.ext.declarative import declared_attr

class BaseMixin:
    """
    AbstractModel.
    Provides standard audit fields to all models.
    """
    id = Column(Integer, index=True, primary_key=True, nullable=False, unique=True, autoincrement=True)
    is_active = Column(Boolean, server_default="True", nullable=False)
    
    # create_date and write_date logic
    create_date = Column(TIMESTAMP(timezone=True), server_default=text("NOW()"), nullable=False)
    write_date = Column(
        TIMESTAMP(timezone=True), 
        server_default=text("NOW()"), 
        onupdate=text("NOW()"), # Automatically updates on every 'write'
        nullable=False
    )
