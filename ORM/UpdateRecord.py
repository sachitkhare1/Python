import psycopg2
def update_query ( id, name ) :
 try  :

    connection = psycopg2.connect (database ="bittoodb", user ="bittoo" , password ="12345" , host ="localhost" , port ="5432")
    cursor = connection.cursor()

    update_qy="""UPDATE student SET name =%s WHERE id =%s"""

    cursor.execute(update_qy ,(name, id))
    connection.commit()
   
    print("Data Update Successfully...")

 except Exception as ex :
    print ("failed to Update data into student table ",ex)

 finally :
    if connection :
        cursor.close()
        connection.close()

update_query(1,'saksham')