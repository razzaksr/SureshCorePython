# reading: r mode

#obj=open("mybasic.doc","r")

#obj=open("D:\Course backups\Python\sureshpython.txt","r")

obj=open("D:\Course backups\Web\Hajan\Form1.html","r")

# data=obj.read()
# print(data)

data=obj.read(100)
print(data)

obj.close()