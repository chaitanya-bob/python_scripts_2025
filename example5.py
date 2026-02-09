import os
#help(os)

#print(dir(os))
print(os.getcwd())
#os.chdir("/home/ubuntu")
print(os.getcwd())
print(os.listdir())

os.makedirs("/home/ubuntu/dir1",exist_ok=True)

if os.path.isfile("/homeubuntu/example5.py"):
    print("file exist")
else:
    print("doesnot exist")
if os.path.exists("dir1"):
    print("directory exist")
else:
    print("doesnot exist")

for curr_pa,dirs,files in os.walk("/root"):
    print(curr_pa,dirs,files) 
print(os.path.basename("/home/ubuntu/tmp"))

