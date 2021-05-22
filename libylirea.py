#with open('readwritepython.txt')as f:
f = open("readwritepython.txt", "r")
#line=f.seek(3)
#line=f.readlines()
#for l in line:
line=f.readlines(1)
line=f.readlines(2)
line=f.readlines(3)
print(line)
f.close()
