import mysql.connector

con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="school_db")

c=con.cursor()

query='''update student set name=%s where roll_no=%s'''
data=("Ram",101)
c.execute(query,data)
con.commit()
print("Data updated successfully")

if c.rowcount>0:
    print("rec updated")
    query='''select * from student where roll_no=%s'''
    data=(101,)
    c.execute(query,data)
    rec=c.fetchall()
    for row in rec:
        print(row)
else:
    print("No rec found")


c.close()
con.close()