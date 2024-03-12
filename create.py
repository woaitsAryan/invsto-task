import pandas as pd
from model import Base, HINDALCO
from db import engine
from db import Session
from validate import validate_data

Base.metadata.create_all(engine)

session = Session()

df = pd.read_csv('stocks.csv')

df['datetime'] = pd.to_datetime(df['datetime'])

data = df.to_dict(orient='records')

validate_data(data)

session.add_all([HINDALCO(**row) for row in data])

session.commit()