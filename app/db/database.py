import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Float, String, DateTime, Boolean
import zipfile
from app.core.config import settings
from utils.dataframe import df_edit

try:
    df = pd.read_csv('doc_tasks.csv')
    df.drop('Unnamed: 0', axis=1, inplace=True)
except FileNotFoundError:
    archive = zipfile.ZipFile('doc_tasks.zip', 'r')
    csv_file = archive.open('doc_tasks.csv')
    df = df_edit(pd.read_csv(csv_file))
    df.to_csv('doc_tasks.csv')

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL
)

with engine.connect() as con:
    con.execute("ALTER DATABASE ocm SET datestyle TO 'Postgres, Euro';")

df.to_sql(
    "document",
    engine,
    if_exists='append',
    index = False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
