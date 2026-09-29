import mysql.connector

con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="school_db")
c=con.cursor()

query='''select * from student'''
c.execute(query)

records=c.fetchall() #result of query comes to code and is assigned to records variable

if records:
    for row in records:
        print(row)
else:
    print("No records found")

c.close()
con.close()