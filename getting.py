# users desired travel location

location=input("tell us your desired vaction place ")
spots=[input("Tell us first spot in your vacation "),
       input("Tell us second spot in your vacation "),
       input("Tell us third spot in your vacation "),]
stay=int(input("Tell us no of days of stay "))
budget=float(input("Tell us budget to travel this vaction place "))

print("Thanks for showing interest to fill your desired location",
      location,"with the major spots",spots
      ,"for the days of",stay,"in budget amount",
      budget,"we wish your desire come true")