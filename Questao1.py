import os

def listar_arquivos(diretorio):
    try:
        for item in os.listdir(diretorio):
            caminho_item = os.path.join(diretorio, item)
            if os.path.isdir(caminho_item):
                print(f'Diretório: {caminho_item}')
                listar_arquivos(caminho_item)
            else:
                print(f'Arquivo: {caminho_item}')
    except PermissionError:
        print(f'Permissão negada para acessar: {diretorio}')
    except FileNotFoundError:
        print(f'Diretório não encontrado: {diretorio}')

diretorio_inicial = 'C:/Users//luizc/OneDrive/Documentos/Workspace'  
listar_arquivos(diretorio_inicial)
