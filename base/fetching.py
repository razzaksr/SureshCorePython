from pymysql import *

conObj=connect(host='localhost',user='root',password='',db='suresh')

curObj=conObj.cursor()

# qry="select * from apartment"
# curObj.execute(qry)
# res=curObj.fetchall()
# for one in res:print(one[0]," ",one[1]," ",one[2]," ",one[3]," ",one[4]," ",one[5])

# qry="select name,salary from apartment"
# curObj.execute(qry)
# res=curObj.fetchall()
# for one in res:print(one[0]," ",one[1])

# qry="select * from apartment where name like 'S%'"
# curObj.execute(qry)
# res=curObj.fetchall()
# for one in res:print(one[0]," ",one[1]," ",one[2]," ",one[3]," ",one[4]," ",one[5])

# qry="select * from apartment where name like '%S'"
# curObj.execute(qry)
# res=curObj.fetchall()
# for one in res:print(one[0]," ",one[1]," ",one[2]," ",one[3]," ",one[4]," ",one[5])

qry="select * from apartment where id=2"
curObj.execute(qry)
one=curObj.fetchone()
print(one[0]," ",one[1]," ",one[2]," ",one[3]," ",one[4]," ",one[5])

print("Record has extracted")