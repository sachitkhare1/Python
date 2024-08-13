from sqlalchemy import create_engine
# import psycopg2

# import urllib.parse

# urllib.parse.quote_plus("postgres")

# user ='postgres'
# host = 'localhost'
# port = '5432'
# database = 'sachit'

# engine = create_engine('postgresql+psycopg2://bittoo:12345@localhost:5432/bittoodb')

# try :

#     with engine.connect() as connection_str :
#         print('Succefully conneted to postgresql Database ')

# except Exception as ex :
#     print(f'Sorry Connection Failed :{ex}')

# from sqlalchemy import create_engine
# import psycopg2

# database = 'sachit'
# user = 'sachit'
# password = '12345'

# connection = psycopg2.connect(database=database, user=user, password=password)

# cursor = connection.cursor()

# create_table = "CREATE TABLE testing_members (id SERIAL PRIMARY KEY, name VARCHAR(25) NOT NULL)"

# cursor.execute(create_table)


# -----------------------------------------------------
import psycopg2

from psycopg2 import sql, Error 

database = 'bittoodb'
user = 'bittoo'
password = '12345'

try:
   
    engine = create_engine('postgresql+psycopg2://bittoo:12345@localhost:5432/bittoodb')
    connection = engine.row_connection()
    cursor = connection.cursor()

    create_table = """
    CREATE TABLE IF NOT EXISTS company (
        id SERIAL PRIMARY KEY,
        name VARCHAR(25) NOT NULL
    )
    """
    
    cursor.execute(create_table)
    
    connection.commit()
    
    print("Table created successfully.")

except (Exception, Error) as error:
    print("Error while creating table:", error)


# import sqlalchemy
# import pandas as pd

# dbEngine=sqlalchemy.create_engine('sqlite:////home/stephen/connect.db') 


# pd.read_sql('select * from test',dbEngine)

# df_todb.to_sql(name = 'use_table',con= dbEngine, index=False, if_exists='replace') 
