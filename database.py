# from deta import Deta

# deta = Deta("c09t829x_6gCdg6KYqRp71yN265RS4EWeE2771GUz")
# db = deta.Base("ScanKuy_db")
# db.put({"name": "alex", "age": 77})

# fetch_res = db.fetch({"name": "Geordi"})
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root@localhost/rpl")

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, bind=engine)