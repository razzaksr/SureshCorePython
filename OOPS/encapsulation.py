# Encapsulation: 
#   data hidding >> even though object created to the class directly, can't access the data/var/object
#   but can access functions

class Mobile:
    #brands=""
    def __init__(self,mod="",bnd="",cost=0,feat=""):
        self.__model=mod
        self.__brand=bnd
        self.__price=cost
        self.__features=feat
    
    def setModel(self,mod=""):self.__model=mod
    def setBrand(self,bnd=""):self.__brand=bnd
    def setPrice(self,cost=0):self.__price=cost
    def setFeatures(self,feat=""):self.__features=feat
    
    def getModel(self):return self.__model
    def getBrand(self):return self.__brand
    def getPrice(self):return self.__price
    def getFeatures(self):return self.__features
    
    def __str__(self):
        return self.__model+" "+self.__brand+" "+self.__features+" "+str(self.__price)
    
    
    
        

# initialize via constructor
mob1=Mobile("5S","Realme",8999,"128GB Internal")
print(mob1.getBrand(),mob1.getFeatures(),mob1.getModel(),mob1.getPrice())

mob2=Mobile()
print(hasattr(mob2,"__brands"))
mob2.setBrand("Nokia")
mob2.setFeatures("64 Internal")
mob2.setModel("6.1Plus")
mob2.setPrice(9888)
print(mob2)

#print(hasattr(mob2,"brands"))



