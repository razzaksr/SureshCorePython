try:
    hello=int(input("Enter the number "))
    print(hello*2)
except ValueError as v:
    print(v)
    hello=int(input("Enter the value as numeric not character "))
    print(hello*2)
    
print("Reached the end")