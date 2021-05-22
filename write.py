#f = open("readwritepython.txt", "a")
#f.write("Now the file has more ")
f = open("readwritepython.txt", "w")
f.write('kalyan \npushpa \nvinnu')
f = open("readwritepython.txt", "r")
print(f.read())
f.close()

#with open('readwritepython') as f:

