# ______________ 69 day ________________ #

#File Handling

f = open("demofile.txt", "rt") 
f = open("demofile.txt", "r")

print(f.read())

print(f.read(5))


f = open("demofile.txt","r")
print(f.readline())
print(f.readline())


f = open("demofile.txt","r")
for x in f:
    print(x)


f = open("demofile.txt","r")
print(f.readline())
f.close()


f = open("demofile2.txt","a")
f.write("Now the file has more content")
f.close()

f = open("demofile2.txt","r")
print(f.read())


f = open("demofile3.txt", "w")
f.write("Woops!! I've deleted the content")

f.close()

f = open("demofile3.txt", "r")
print(f.read())

##f = open("myfile.txt", "x")

import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does't exist")


import os
os.rmdir("myfolder")


