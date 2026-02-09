def writefile():
    with open("2.txt", 'a') as fh:
         fh.write("\nwelcome\n")
         fh.write("hi\n")


def readfile():
    with open("2.txt", 'r') as fh:
         content=fh.read()
         print(content)

readfile()
writefile()
