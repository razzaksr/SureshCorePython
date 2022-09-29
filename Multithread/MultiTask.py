from threading import *

class House:
    click=[45,90,11,34,2.34,6.7,6.5,66,4,54,4,54.5,6.76,6,5]

class Alpha(Thread,House):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        print("welcome",self.name)
        self.click.sort()
        for x in self.click:print(x)
        
class Beta(Thread,House):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        lk.acquire()
        print("Welcome",self.name)
        pos=int(input("Tell us position to delete"))
        self.click.pop(pos)
        for x in self.click:print(x)
        lk.release()
        
lk=Lock()
        
a1=Alpha("Vinayak")
a2=Alpha("Anand")
b1=Beta("Tarun")
b2=Beta("Bajaj")

a1.start()
a2.start()
b1.start()
b2.start()