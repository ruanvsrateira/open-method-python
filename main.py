import os

while True:
  try:  
    mode = int(input("Insira o código referente a sua ação \n[0] ler conteúdo do arquivo\n[1] criar arquivo\n[2] sair\n"))

    match(mode):
      case 0: 
        archive_name = str(input("Insira o nome do arquivo a ser lido (OBS: o arquivo deve estar na pasta onde está o arquivo main.py): "))
        try:
          with open(archive_name, "r") as archive:
            print(f"\nConteúdo do arquivo: \n{archive.read()}\n")
        except FileNotFoundError:
          print("Arquivo não encontrado")
      case 1: 
        name_file = str(input("Digite o nome do arquivo.[extensão]: "))
        content = str(input("Digite o conteúdo que haverá no arquivo: "))
        if not name_file in os.listdir():
          with open(name_file, "x") as archive:
            archive.write(content)
        else:
          with open(name_file, "r") as archive:
            print(f"\nO arquivo {name_file} já existe\nConteúdo do arquivo: \n{archive.read()}\n")
      case 2:
        break
      case _:
        continue
  except:
    print("\nTente novamente!\n")
    continue