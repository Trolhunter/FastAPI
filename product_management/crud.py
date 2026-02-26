from sqlalchemy.orm import Session, sessionmaker

import models,schema
from fastapi import HTTPException

# company crud

def get_company(db: Session,company_id: int) -> type[models.Company] | None:
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def get_companies(db:Session,skip: int = 0,limit: int = 100) -> list[type[models.Company]] | None:
    return db.query(models.Company).offset(skip).limit(limit).all()

def create_company(db:Session, company:schema.CompanyCreate):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

