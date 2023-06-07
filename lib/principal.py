from sqlalchemy import  String, Column, Integer , create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///school.db')
Base = declarative_base()

class Principal(Base):
    __tablename__= 'principals'

    principal_id = Column(Integer, primary_key=True)
    principal_reg = Column(Integer)
    principal_school = Column(String(10))
    principal_name = Column(String)
    principal_phone_number = Column(Integer)


Base.metadata.create_all(engine)     