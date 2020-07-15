import os
import glob

#region methods
def getFileExtensionByPath(filePath):
    extension = filePath.split(".")
    return (extension[-1])

def getFileExtensionByName(name):
    extension = name.split(".")
    return (extension[-1])

def getFileName(file):
    name = file.split("\\")
    return name[-1]
#endregion

#region switches
def extensionSwitcher(Extension):
    switcher = {
        "jpg": "imagem",
        "png": "imagem",
        "jpeg": "imagem",
        "pdf": "documento",
        "doc": "documento",
        "pptx": "documento",
        "xlsx": "documento",
        "zip": "compactado",
        "rar": "compactado",
        "exe": "executavel"
    }
    return switcher.get(Extension,"outro")

def typeSwitcher(type):
    switcher ={
        "imagem":"imagens",
        "documento":"documentos",
        "compactado":"compactados",
        "executavel":"executaveis",
        "outro":""
    }
    return switcher.get(type,"")
#endregion

#------------------------------------------

files = glob.glob("*")

for file in files:
    name=getFileName(file)
    extension =getFileExtensionByName(name)
    type = extensionSwitcher(extension)
    destinationPath = f"./{typeSwitcher(type)}/"
    print(destinationPath)

    if not os.path.exists(destinationPath):
        os.makedirs(destinationPath)
        print(f"diretorio {destinationPath} created")
    
    os.rename(file, destinationPath+name)
    print(f"{name} moved")
