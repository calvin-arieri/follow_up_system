from sqlalchemy import  String, Column, Integer , create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///school.db')
Base = declarative_base()

class Full_info:
    pass
