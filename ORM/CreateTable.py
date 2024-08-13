import psycopg2

connection = psycopg2.connect (database ="bittoodb" , user = "bittoo" , password ="12345" , host ="localhost" , port ="5432")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS student")

sql ="""CREATE TABLE student (id INT PRIMARY KEY NOT NULL , name VARCHAR(50) NOT NULL ,city VARCHAR(50) NOT NULL )"""

cursor.execute(sql)
 
print("Table Created successfully ...")

connection.commit()
connection.close()