# abstraction: hiding the logic/body of the function

from abc import *

class Wind(ABC):
    def hello(self):
        print("Non abstract method")
    
    def there(self):
        pass

class Derive(Wind):
    def owm(self):
        print("Derive's own function")
    
    def there(self):
        print("There derived/ overriden from Wind")

d1=Derive()
d1.hello()
d1.owm()
d1.there()

# w1=Wind()

# w1.hello()
# w1.there()