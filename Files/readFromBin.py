from pickle import *

obj=open("mybinaries.txt","rb")

while True:
    try:
        hai=load(obj)
        print(hai)
    except EOFError as e:
        break

obj.close()