from sqlalchemy import create_engine,URL
from sqlalchemy.orm import sessionmaker,scoped_session,declarative_base

user = 'postgres'
password = 'Admin@123'
host = '127.0.0.1'
port = 5432
database = 'fa_ecommerce_test'

def get_connection():
    url_obj = URL.create(
        drivername='postgresql+psycopg2',
        username=user,
        password=password,
        host=host,
        port=port,
        database=database
    )
    return create_engine(
        url=url_obj,future=True
    )


SessionLocal = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=get_connection()
)
)

# Base class for models
Base = declarative_base()
