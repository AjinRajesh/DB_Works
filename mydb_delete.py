import mysql.connector

con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="school_db")

c=con.cursor()

query='''delete from student where roll_no=%s'''
data=(102,)

c.execute(query,data)
con.commit()

if c.rowcount>0: #if any change occured row count increases from zero. so that means deletion occurs
    print("Data is deleted")
else:
    print("No record deleted because record not found")

c.close()
con.close()