import mysql.connector

con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="school_db")

c=con.cursor()

query='''select * from student where roll_no=%s;'''

data=(101,)

c.execute(query,data)
rec=c.fetchone() # fetch a single data

if rec:
    for row in rec:
        print(row)
else:
    print("No record found")

c.close()
con.close()