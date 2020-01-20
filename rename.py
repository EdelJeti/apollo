import os
# little python script to rename some image files

path = os.chdir("/home/user/images/heic")

i = 1145

for file in os.listdir(path):
    
    new_file_name = "pic{}.jpg".format(i)
    
    os.rename(file, new_file_name)
    
    i = i+1
    print (new_file_name)

print ("done")