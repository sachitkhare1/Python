from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)


DATABASE_URL = 'postgresql://bittoo:12345@:5432/bittoodb'
engine = create_engine(DATABASE_URL)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


new_person = Person(name='John Doe')
session.add(new_person)
session.commit()


# person = session.query(Person).filter_by(name='John Doe').first()
# print(person.id, person.name)



# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine , Column , Integer , Table , MetaData, ForeignKey ,CHAR, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# Base = declarative_base()


# class Person(Base):
#     __tablename__ = 'faltu'

#     id =Column ("ID" ,Integer ,primary_key=True)
#     First_name = Column ("First_name" , String)
#     Last_name = Column ("Last_name" , String)
#     gender = Column ("Gender" , String)
#     age = Column ("age", Integer)


#     def __init__(self , id_ , First , last , gender , age ) :
#         self.id= id_
#         self.First_name = First
#         self.Last_name = last
#         self.gender = gender
#         self.age =age

#     def __repr_(self) :
#         return f"({self.id}) {self.First_name} {self.Last_name} ({self.gender} {self.age})"
    

# engine = create_engine('postgresql://bittoo:12345@localhost:5432/bittoodb')

# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# person = Person (109 , "sachit" , "khare" , "Male" , 22)
# session.add(person)

# p1 = Person(102 , "bittoo", "gupta" , "Male" , 21)
# p2 = Person (103 ,"Sittu" , "Shrivastava" , "Male" ,17)
# p3 = Person (104 , "himanshu" , "sen" , "Male" , 28) 

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

# result = session.query(Person)
# print(result)


#     db.Table('employee' , metadata,
#                 db.Column( 'id' , db.Integer , primary_key = True),
#                 db.Column('name' , db.String(255) , nullable= False),
#                 db.Column('address' , db.String(255) , nullable= False),
#                 db.Column('city ', db.String(255) , nullable= False)
#                 )

# metadata.create_all(engine)

# query = db.insert(Person).values(id=96, name='Matthew', address ='shree nath city',city ='BIHAR')
# Result = conn.execute(query)

# --------------------------------------------
# -------------- working ---------------------
# --------------------------------------------
# import sqlalchemy as db
# from sqlalchemy import create_engine, Column, Integer, TEXT, Table, MetaData

# engine = db.create_engine('postgresql+psycopg2://bittoo:12345@localhost:5432/bittoodb')

# conn = engine.connect()

# metadata = MetaData()

# employee = Table('employee', metadata, autoload_with=engine)

# print(repr(employee))

# id = employee.columns.keys()

# print(id)

#  ----------------------------------------------
# Not working 
# ------------------------------------------------
# import sqlalchemy as db
# from sqlalchemy import create_engine ,Column,Integer ,TEXT ,Table ,MetaData ,table
# from sqlalchemy.orm import sessionmaker


# engine =db.create_engine('postgresql+psycopg2://bittoo:12345@localhost:5432/bittoodb')

# conn = engine.connect()

# metadata = db.MetaData()

# division= db.Table('profile', metadata, autoload=True, 
# autoload_with=engine) 

# print(repr(metadata.tables['profile']))


# Table ('profile', MetaData() , Column('email',TEXT(), table=<profile>) , Column ('name' , TEXT() ,table=<profile> , Column('contact' ,Integer , table=<profile>) ) , schema =None)

# Table ('profile', MetaData(), Column('email', TEXT(),table=<profile>), 
# Column('name', TEXT(), table=<profile>), Column('contact', Integer, 
# table=<profile>), schema=None)

# print(email.columns.keys())

