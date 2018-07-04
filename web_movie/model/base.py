from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('postgresql://test:123456@localhost:5432/test2')
Base = declarative_base()
metedata = MetaData(engine)


