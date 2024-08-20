# from sqlalchemy.orm import sessionmaker
# import sqlalchemy as db
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Actor(Base) :

#     _table_args_ = {'schema' : 'bittoo' }
#     _table_name_ = 'person'

#     p_id = db.Column ( db.SmallInteger , autoincrement=True , primary_key=True )
#     first_name = db.Column ( db.String(45) , nullable= False )
#     last_name = db.column ( db.String(45) , nullable= False )
#     last_update = db.column (db.TIMESTAMP , nullable = False , server_default= db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

# engine = db.create_engine('postgresql+psycopg2://bittoo:12345@localhost:5432/bittoodb')    

# Session = sessionmaker (bind=engine)
# session = Session()


# result = session.query(Actor).count()

# print("count of the actor " , result)
# print(type(Actor))

# showing error--------------------------------------------

from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

Base = declarative_base()

class Actor(Base):
    __tablename__ = 'person'

    p_id = db.Column(db.SmallInteger, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    last_update = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())


engine = db.create_engine('postgresql+psycopg2://bittoo:12345@localhost:5432/bittoodb')


Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Actor).count()

print("Count of the actor:", result)
print(type(Actor))
