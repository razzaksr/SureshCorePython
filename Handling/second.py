hai=[23.5,6.98,5,12,44,5,8,0,87,'Razak']

try:
    pos=int(input("Tell us position "))

    print(hai[pos]/2)
except TypeError as obj:
    print(obj,"\nEnter the position not 9th one ")
    pos=int(input("Tell us position "))
    print(hai[pos]/2)