from pymysql import *

conObj=connect(host='localhost',user='root',password='',db='suresh')

curObj=conObj.cursor()

#insertion/update/delete
conObj.autocommit(True)

qry="truncate table apartment"

curObj.execute(qry)

print("Records are deleted")