from sqlalchemy import  String, Column, Integer , create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///school.db')
Base = declarative_base()

class Other_user(Base):
    __tablename__ = 'other_users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    user_password = Column(String(20))
    company_name = Column(String(20))

Base.metadata.create_all(engine)
