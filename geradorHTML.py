# Solicitar o nome do arquivo HTML
nome_arquivo = input("Digite o nome do arquivo HTML (inclua a extensão .html): ")

# Solicitar o título da página
titulo = input("Digite o título da página: ")

# Solicitar o conteúdo da página
conteudo = input("Digite o conteúdo da página (parágrafos, links, etc.): ")

# Criar o arquivo HTML e escrever o conteúdo
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(f'<!DOCTYPE html>\n<html>\n<head>\n\t<title>{titulo}</title>\n</head>\n<body>\n{conteudo}\n</body>\n</html>')

print(f'Arquivo HTML "{nome_arquivo}" criado com sucesso.')
