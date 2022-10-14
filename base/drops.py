from pymysql import *

# conObj=connect(host='localhost',user='root',password='',db='suresh')
# curObj=conObj.cursor()
# #insertion/update/delete
# conObj.autocommit(True)
# qry="drop table apartment"
# curObj.execute(qry)
# print("Table deleted")

conObj=connect(host='localhost',user='root',password='')
curObj=conObj.cursor()
#insertion/update/delete
conObj.autocommit(True)
qry="drop database suresh"
curObj.execute(qry)
print("Databse deleted")