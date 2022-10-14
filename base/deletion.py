from pymysql import *

conObj=connect(host='localhost',user='root',password='',db='suresh')

curObj=conObj.cursor()

#insertion/update/delete
conObj.autocommit(True)

# qry="delete from apartment where id=3"
# curObj.execute(qry)
# print("Record are deleted")

qry="delete from apartment where name like '%s%'"
curObj.execute(qry)
print("Record are deleted")