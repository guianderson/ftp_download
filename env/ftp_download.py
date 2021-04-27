from ftplib import FTP
from os.path import exists


nonpassive = False

dir_nome = '/terrama2q/TerraMA2Q_408'
site_nome = 'ftp.dgi.inpe.br'

usuario_info = ('queimadas', 'inpe_2012')

conexao = FTP(site_nome)
conexao.login(*usuario_info)
conexao.cwd(dir_nome)

print(conexao.retrlines('LIST'))
nome_arquivo = input('Insira o nome do arquivo que deseja realizar o download: ')

if nonpassive:
    conexao.set_pasv(False)

conexao.retrbinary("RETR " + nome_arquivo, open(nome_arquivo, "wb").write)

