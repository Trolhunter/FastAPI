from fastapi import FastAPI,Depends,HTTPException
import schema,crud
from database import get_connection,Base,SessionLocal
from sqlalchemy.orm import Session
from typing import List
Base.metadata.create_all(bind=get_connection())

app = FastAPI(title="Warehouse Management API's")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/companies/", response_model=schema.CompanyRead)
def create_company(company: schema.CompanyCreate, db: Session = Depends(get_db)):
    """Create a new Company record"""
    return crud.create_company(db=db, company=company)

@app.get("/companies/", response_model=List[schema.CompanyRead])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Fetch all Company records"""
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies

@app.get("/companies/{company_id}", response_model=schema.CompanyRead)
def read_company(company_id: int, db: Session = Depends(get_db)):
    """Fetch a single Company by ID"""
    db_company = crud.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company