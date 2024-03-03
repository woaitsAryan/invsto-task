from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="pgpass",
    host="localhost",
    port=5432,
    database="postgres"
)

engine = create_engine(url)

Session = sessionmaker(bind=engine)