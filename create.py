import pandas as pd
from model import Base, HINDALCO
from db import engine
from db import Session

Base.metadata.create_all(engine)

session = Session()

df = pd.read_csv('stonks.csv')

data = df.to_dict(orient='records')

session.add_all([HINDALCO(**row) for row in data])

session.commit()