import psycopg2
def Delete_query ( id) :
 try  :

    connection = psycopg2.connect (database ="bittoodb", user ="bittoo" , password ="12345" , host ="localhost" , port ="5432")
    cursor = connection.cursor()

    delete_qy="""DELETE FROM student WHERE id =%s"""

    cursor.execute( delete_qy,(id,))
    connection.commit()
   
    print("Data Deleted Successfully...")

 except Exception as ex :
    print ("failed to Delete data from student table ",ex)

 finally :
    if connection :
        cursor.close()
        connection.close()

Delete_query(2)