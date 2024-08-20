from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://bittoo:12345@localhost:5432/bittoodb')

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

class Employee1(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    value = Column(Integer)

Base.metadata.create_all(engine)

session.add(Employee1(value=1))
session.add(Employee1(value=2))
session.add(Employee1(value=3))
session.commit()

results = session.query(Employee1).filter(Employee1.value * 2 > 3).all()

for result in results:
    print(result.value)


