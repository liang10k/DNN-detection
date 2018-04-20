import os
os.chdir("/Users/mtoasf/Desktop/images")
print(os.getcwd())
i=0
for f in os.listdir():
    #file_name,file_ext = os.path.splitext(f)
    #file_name = file_name.strip() # drop the space left or right
    a=str(i)
    a=a.strip().zfill(6)
    #print("{}{}".format("00000",a))
    print(a)
    file_ext=".png"
    new_name = "{}{}".format(a,file_ext)
    print(new_name)
    os.rename(f,new_name)
    i=i+1