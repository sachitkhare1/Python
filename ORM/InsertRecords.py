import psycopg2

try  :

    connection = psycopg2.connect (database ="bittoodb", user ="bittoo" , password ="12345" , host ="localhost" , port ="5432")
    cursor = connection.cursor()

    insert_query="""INSERT INTO student (id , name , city) values (%s,%s,%s)"""

    values = [ (2, 'sachit', 'Lalitpur') , ( 2 ,'Bittoo', 'Jhansi') , (3 , 'kapil' , 'Indore')]
   
    for i in values :
       cursor.execute(insert_query ,i )

       connection.commit()
       count =  cursor.rowcount

    print (count , "records inserted into student Tables.")

except Exception as ex :
    print ("failed to Insert data into student table ",ex)

finally :
    if connection :
        cursor.close()
        connection.close()