from sqlalchemy import  String, Column, Integer , create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    student_id= Column(Integer, primary_key= True)
    student_first_name = Column(String(15))
    student_second_name = Column(String(10))
    student_surname = Column(String(10))
    school_code = Column(String)
    unique_code = Column(String)

class Parent(Base):
    __tablename__ = 'parents'

    parent_id = Column(Integer, primary_key=True)
    parent_name = Column(String)
    parent_phone = Column(String)  
    student_code = Column(String)
    parent_log_in = Column(String) 
      
Base.metadata.create_all(engine)

