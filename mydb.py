import mysql.connector
#
# con=mysql.connector.connect(user="root",password="ajin",host="localhost")
# print(con)
#
# #cursor object -- for executing sql queries
# c=con.cursor()
#
# #query for creating db file
# query="create database school_db"
# c.execute(query)
# print("database file created")
#
# c.close()
# con.close()


con=mysql.connector.connect(user="root",password="ajin",host="localhost",database="school_db")

c=con.cursor()

#query
# query="""create table student(roll_no int not null primary key,
#                               name varchar(50),
#                               age int,
#                               place varchar(50),
#                               phone varchar(50),
#                               total_mark int);"""
#
# c.execute(query)
# print('table created')

query="""insert into student values(%s,%s,%s,%s,%s,%s);"""
data=(101,"Arun",11,"ekm","1324532",145)

c.execute(query,data)
con.commit() #permanently saves data into db

data=(102,"Ajin",23,"kannur","432134",150)
c.execute(query,data)
con.commit()
print("inserted data succesfully")

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