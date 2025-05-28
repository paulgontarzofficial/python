import os 

#process = os.getpid()
#directories = os.listdir()

#print(directories)
# print(process)


# Declare the uname variable 
uname = str(os.uname())

# Specifying the file that we would like to write our information to. 
file = open("sysinfo.txt", "w")
file.write(uname)
file.close()

# Writing group information 
groups = os.getgroups()
for i in groups:
    file = open("sysinfo.txt", "a")
    i = str(i)
    file.write("\n")
    file.write(i)    


# for i in uname:
#     output = i
#     if os.path.exists("sysinfo.txt"): 
#         f = open("sysinfo.txt", "w")
#         f.write(output)
#     else:
#         f = open("sysinfo.txt", "a")
#     print(i)