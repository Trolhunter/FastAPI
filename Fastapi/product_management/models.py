from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, CheckConstraint,ForeignKey
from sqlalchemy.types import Integer,String,Float,DateTime,Boolean,Text
from datetime import datetime



class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True,index=True,nullable=False,autoincrement=True)
    name = Column(String(30),name='Name',nullable=False)
    description = Column(String(255),name="description")
    create_date = Column(DateTime,default=datetime.now,name='Create Date')
    warehouse_ids = relationship('Warehouse',backref='company')
    location_ids = relationship('Location',backref='company')

class Warehouse(Base):
    __tablename__ = 'warehouse'

    id = Column(Integer, primary_key=True,index=True,nullable=False,autoincrement=True)
    name = Column(String(30),name='Name',nullable=False)
    description = Column(String(255),name="description")
    company_id = Column(Integer, ForeignKey('company.id'),nullable=False)
    location_ids = relationship('Location',backref='warehouse')
    create_date = Column(DateTime,default=datetime.now,name='Create Date')


class Location(Base):
    __tablename__ = 'warehouse_location'

    id = Column(Integer, primary_key=True,index=True,nullable=False,autoincrement=True)
    name = Column(String(30),name='Name',nullable=False)
    description = Column(String(255),name="description")
    company_id = Column(Integer, ForeignKey('company.id'),nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'),nullable=False)
    create_date = Column(DateTime,default=datetime.now,name='Create Date')
    product_ids = relationship('ProductTemplate',backref='warehouse_location')


class ProductTemplate(Base):
    __tablename__ = 'product_template'

    id = Column(Integer, primary_key=True,index=True,nullable=False,autoincrement=True)
    name = Column(String(30),name='Name',nullable=False)
    description = Column(String(255),name="description")
    price = Column(Float,default=0.0,name='price')
    on_hand_qty = Column(Integer,name="Quantity",default=0)
    is_active = Column(Boolean,default=True,name="Active")
    create_date = Column(DateTime,default=datetime.now,name='Create Date')
    company_id = Column(Integer, ForeignKey('company.id'),nullable=False)
    location_id = Column(Integer, ForeignKey('warehouse_location.id'),nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'),nullable=False,)

    __table_args__ = (
        CheckConstraint('price >= 0.0',name='check_price_positive'),
    )
