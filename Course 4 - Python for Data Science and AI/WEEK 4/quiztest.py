with open("example1.txt", 'w') as file1:
    file1.write("This is the first line written.\n")

with open("example1.txt", 'r') as testread:
    print(testread.read())
    
with open("example1.txt","a") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

with open("example1.txt", 'r') as testread1:
    print(testread1.read())

