import psycopg2

try  :

    connection = psycopg2.connect (database ="bittoodb", user ="bittoo" , password ="12345" , host ="localhost" , port ="5432")
    cursor = connection.cursor()

    select_qy="""SELECT * FROM student"""

    cursor.execute(select_qy)
    records = cursor.fetchall()

    for i in records :
       
       print( "Id" ,i[0] )
       print( "Name" ,i[1])
       print( "City" ,i[2])
       print()

    connection.commit()

except Exception as ex :
    print ("failed to fatch from student table ",ex)

finally :
    if connection :
        cursor.close()
        connection.close()

