import os

# loop through directory


files=os.listdir()

for file in files:
    if os.path.splitext(file)[1] ==".py":
        with open(file,"r") as f1:
            c=f1.read()
            f1.close()
            if c.__contains__("__name__"):
                print("skipped")
                
            else:
                with open(file,"a+") as f:
                    print(f.readline())
                    if f.read().__contains__("__name__"):
                        f.write("\nif __name__ == '__main__' : \n \tprint('main fucntion loaded')")
    else:
        pass
 

if __name__ == '__main__' : 
 	print('main fucntion loaded')
