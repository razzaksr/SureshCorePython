# water bottle details

bottle={
    "model":"D-Mart sportz",
    "price":200,
    "colors":['blue','red','purple','pink','yellow'],
    "sizes":(1000,500,750,200,300,600),
    "materials":{"Stainless steel","plastic"}
}

#print(bottle)
#print(type(bottle))
print(bottle['model'])# str
print(bottle['price'])# int
print(bottle['colors'])# list
print(bottle['sizes'])# tuple
print(bottle['materials'])# set

print(bottle['colors'][1])
print(bottle['sizes'][0])
