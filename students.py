from sqlalchemy import  String, Column, Integer , create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///school.db')
Base = declarative_base

class Student(Base):
    __tablename__ = 'students'

    student_id= Column(Integer, primary_key= True)
    student_first_name = Column(String(10))
    student_second_name = Column(String(10))
    student_surname = Column(String(10))
    student_unique_code = Column(String(10))
    parent_first_name = Column(String(10))
    parent_second_name = Column(String(10))
    parent_surname = Column(String(20))
    parent_phone_number = Column(String(20))
