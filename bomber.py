import platform
import os
import random

os_name=platform.system()


class malicious():
    
    def __init__(self):
        self.os=platform.system()
        self.default_path="/"
        self.string_options="godfreywekesa1234567890"
        self.formats=["png","jpeg","py","docx","c","java","js","html","css","bat","inf","cpp","dockerFile"]
        self.n=50
        self.main();
    def init__(self):
        files=os.listdir("/")
        if platform.system() =="Windows":
            self.default_path=os.path.join("C:\\Users",get_user())
            
        elif platform.system() =="Linux":
            self.default_path="/"
        if "home" in files:
            self.default_path=os.path.join(self.default_path,"home")
            files=os.listdir(self.default_path)
            if len(files)> 0:
                self.default_path=os.path.join(self.default_path,files[0])
                print(self.default_path)
    def get_user(self):
        os.system("net user > net.txt")
        if os.path.exists("net.txt"):
            with open("net.txt","r") as f:
                content=f.read()
                lines=content.split("\n\n")
                user=lines[1].split("\n")[2].split("       ")[0].strip()
                return user
    def generate_name(self):
        num_choices = 10  # Number of random choices you want to generate
        random_choices =''.join (random.choices(self.string_options, k=num_choices))
        filename=random_choices+"."+self.formats[random.randint(0,len(self.formats)-1)]
        return filename
    def create_random_files(self,path):
        try:
            print("creating files")
            for n in range(self.n):
                with open(os.path.join(path,self.generate_name()),"w") as f:
                    f.write("")
                    f.close()
        except Exception as e:
            print("",e)
    def main(self):  
        self.init__()
        path=""
        if platform.system() =="Linux":
            path="Desktop\stupid2\logs"
        elif platform.system()== "Windows":
            path="Desktop/stupid2/logs"
        full_path=os.path.join(self.default_path,path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print("directories created")
            self.create_random_files(path=full_path)
        else:
            self.create_random_files(path=full_path)

            
malicious()
