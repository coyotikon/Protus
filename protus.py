import webbrowser
import random
import time
from colorama import Fore
import os
import wikipedia
import datetime
import socket
import ping3
import openai

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return str(e)

def scan_network(ip_range):
    local_ip_parts = ip_range.split('.')
    base_ip = '.'.join(local_ip_parts[:3]) + '.'

    devices = []
    for i in range(1, 255):
        target_ip = base_ip + str(i)
        if target_ip != get_local_ip():  # Exclude own device
            try:
                host_name = socket.gethostbyaddr(target_ip)
                devices.append({'ip': target_ip, 'hostname': host_name[0]})
            except socket.herror:
                pass

    return devices



def save_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)
def main():
    print("BLOCO DE NOTAS")
    print("Digite seu texto. Para salvar, digite 'salvar' em uma nova linha.")
    
    content = []
    while True:
        line = input()
        if line.lower() == "salvar":
            file_path = input("Digite o caminho do arquivo para salvar (exemplo: 'arquivo.txt'): ")
            save_file("\n".join(content), file_path)
            print(f"Arquivo salvo em '{file_path}'")
            break
        content.append(line)

def contar_piada():
    piadas = [
        # Piadas sobre animais
        "Por que os cientistas não confiam nos átomos? Porque eles compõem tudo!",
        "Por que alguns casais não vão à academia? Porque alguns relacionamentos não dão certo!",
        "Por que o espantalho ganhou um prêmio? Porque ele era excepcional em seu campo!",
        "Por que o livro de matemática estava triste? Porque tinha muitos problemas!",
        "Por que os esqueletos não lutam entre si? Porque são uns frangos!",
        "Por que o tomate ficou vermelho? Porque viu o molho de salada!",
        "Por que os vampiros não têm muitos amigos? Porque são um incômodo!",
        "Qual é o cúmulo do absurdo? Jogar uma bomba de confete!",
        "O que o zero disse para o oito? Que cinto maneiro!",
        "Por que o cachorro entrou no cinema? Para pegar um filhote.",
        # Piadas sobre frutas
        "Por que a laranja foi para a escola? Para aprender a ser suco!",
        "O que a banana suicida falou? Macacos me mordam!",
        "O que o morango disse para o chantilly? Ei, você está me cobrindo!",
        "Por que a uva foi parar no hospital? Porque estava passando mal.",
        "O que a uva verde falou para a uva roxa? Respira!",
        "Qual a fruta mais calma? O maracujá.",
        "O que a maçã disse para a pera? Desencana, você não faz o meu tipo.",
        "Por que a melancia estava brava? Porque a cortaram.",
        "Por que o abacaxi não pode ser goleiro? Porque ele tem medo da trave.",
        "Qual é o dia preferido das frutas? Sexta-feira.",
        # Piadas sobre legumes
        "O que a cenoura disse para o pepino? Você é um picles!",
        "O que o feijão disse para o arroz? Já está de saco cheio de mim?",
        "Por que o tomate virou ketchup? Porque pisaram nele.",
        "O que a batata doce disse para a batata inglesa? Sorria, você é assada!",
        "Por que a ervilha não gosta de sair? Porque tem medo de ser esmagada.",
        "O que o milho falou para a pipoca? Vai na frente, que eu estouro atrás.",
        "Por que o espinafre não mente? Porque é cheio de fibra.",
        "O que o brócolis disse para a couve-flor? Nossa, como você é branca!",
        "Qual é o legume mais divertido? A abobrinha.",
        "Por que o pepino é bom em contar segredos? Porque ele é um conservador.",
    ]

    piada = random.choice(piadas)
    return piada

def abrir_navegador(url):
    webbrowser.open(url)

def tratar_resposta_comando_nao_reconhecido():
    respostas = [
        "Desculpe, não entendi o que você disse. Pode reformular?",
        "Parece que não consegui entender sua solicitação. Poderia tentar novamente?",
        "Me desculpe, mas não consegui compreender o que você disse. Poderia ser mais claro?"
    ]
    return random.choice(respostas)

def responder_saudacao():
    respostas = [
        "Oi! Como posso ajudar você?",
        "Olá! O que posso fazer por você hoje?",
        "Olá, olá! Como posso ser útil?"
    ]
    return random.choice(respostas)

def responder_agradecimento():
    respostas = [
        "De nada! Estou aqui para ajudar.",
        "Não há de quê! Se precisar de mais assistência, é só me chamar.",
        "Sem problema! Se precisar de mais informações, estou à disposição."
    ]
    return random.choice(respostas)

def modo_calculadora():
    print("Modo Calculadora ativado. Para sair, digite 'sair'.")
    while True:
        expressao = input("Digite uma expressão matemática, por exemplo: 72×8: ")
        if expressao.lower() == "sair":
            break
        try:
            resultado = eval(expressao)
            print("Resultado:", resultado)
        except Exception as e:
            print("Erro ao calcular. Certifique-se de usar uma sintaxe válida.")
            print("Erro:", e)

def buscar_wikipedia(termo_pesquisa):
    wikipedia.set_lang('pt')
    try:
        resultado = wikipedia.summary(termo_pesquisa, 2)
        print(resultado)
    except wikipedia.DisambiguationError as e:
        print("A busca retornou múltiplos resultados. Por favor, seja mais específico.")
    except wikipedia.PageError:
        print("Não foi possível encontrar informações sobre o termo pesquisado.")
    except Exception as e:
        print("Ocorreu um erro ao buscar na Wikipedia. Tente novamente mais tarde.")
        print("Erro:", e)

def criar_poema():
    temas = [
        "amor", "natureza", "felicidade", "solidão", "esperança"
    ]
    tema_escolhido = random.choice(temas)
    print(f"Aqui está um poema sobre '{tema_escolhido}':")
    if tema_escolhido == "amor":
        print("Nas asas do vento, nosso amor alçou voo,")
        print("No suave murmúrio do rio, encontramos abrigo.")
        print("Teu olhar é o farol que guia minha jornada,")
        print("E em teus braços, encontro a paz desejada.")
    elif tema_escolhido == "natureza":
        print("No silêncio das florestas, a natureza canta,")
        print("Cachoeiras dançam, a lua brilha e encanta.")
        print("O vento sussurra segredos aos rios serenos,")
        print("E nas montanhas, a beleza se revela em plenos.")
    elif tema_escolhido == "esperança":
        print("Em cada aurora, a esperança renasce,")
        print("Desenhando promessas de um futuro que abraça.")
        print("Mesmo nas sombras, a luz busca seu espaço,")
        print("E o coração humano persiste em seu compasso.")
    elif tema_escolhido == "solidão":
        print("Na vastidão da noite, a solidão me visita,")
        print("Estrelas distantes, testemunhas da minha fita.")
        print("Mas em meio à escuridão, encontro força interior,")
        print("E enfrento a solidão com coragem e amor.")
    elif tema_escolhido == "aventura":
        print("Sob um céu vasto e claro, eu parto em busca de aventura,")
        print("Trilhando caminhos incertos, com coragem e bravura.")
        print("Cada passo é uma jornada, cada escolha, um desafio,")
        print("Pois na busca pela aventura, encontro meu verdadeiro eu.")

    print("Espero que tenha apreciado este poema inspirador!")

def criar_historia():
    temas = [
        "aventura", "mistério", "fantasia", "romance", "ficção científica"
    ]
    tema_escolhido = random.choice(temas)
    print(f"Aqui está uma história do gênero '{tema_escolhido}':")
    if tema_escolhido == "aventura":
        print("Em uma ilha misteriosa, um grupo de exploradores embarca em uma jornada em busca de um tesouro lendário que foi perdido.  Espero que tenha te inspirado.")
    elif tema_escolhido == "mistério":
        print("Um detetive brilhante é chamado para resolver um assassinato em uma mansão isolada, onde todos têm um segredo a esconder. Espero que tenha te inspirado.")
    elif tema_escolhido == "fantasia":
        print("Em um mundo mágico, um jovem órfão descobre que possui habilidades mágicas únicas e parte em uma jornada para salvar seu reino. Espero que tenha te inspirado.")
    elif tema_escolhido == "romance":
        print("Dois estranhos se encontram por acaso em uma estação de trem e, ao longo de uma noite, compartilham histórias de amor e perda. Espero ter lhe inspirado")
    elif tema_escolhido == "ficção científica":
        print("Em um futuro distante, a humanidade colonizou planetas distantes, mas uma ameaça alienígena desconhecida coloca a sobrevivência em risco. Espelho ter lhe inspirado.")

    print("Espero que tenha gostado dessa história emocionante!")
def criar_senha_segura():
    caracteres = "aBbcdeFgHhijKklLmMnoPq24971"
    senha = ''.join(random.choice(caracteres) for _ in range(12))
    print("Senha gerada:", senha)

def aprender_programacao():
    print("Bem-vindo ao modo de Aprendizado de Programação!")
    print(Fore.LIGHTBLACK_EX+"CONCEITOS :                         variável, loop, função")
    print(Fore.LIGHTMAGENTA_EX+"Digite um conceito de programação para aprender sobre ele:")
    conceito = input()
    if conceito == "variável":
        print("Uma variável em programação é um espaço na memória usado para armazenar valores.")
        print("É como uma caixa virtual que pode conter diferentes tipos de dados, como números, texto, etc.")
        print("Exemplo de declaração de variável: idade = 25")
    elif conceito == "loop":
        print("Um loop é uma estrutura de controle que permite repetir um bloco de código várias vezes.")
        print("Um exemplo comum é o loop 'for', que percorre uma sequência de valores.")
        print("Exemplo de loop 'for':")
        print("for i in range(5):")
        print("    print(i)")
    elif conceito == "função":
        print("Uma função é um bloco de código que realiza uma tarefa específica.")
        print("É uma maneira de organizar e reutilizar código.")
        print("Exemplo de função:")
        print("def saudacao(nome):")
        print("    print('Olá, ' + nome)")
        print("saudacao('Maria')")
    else:
        print("Desculpe, ainda não tenho informações sobre esse conceito. Tente outro.")

    print("Espero que essa explicação tenha ajudado você a entender melhor o conceito de programação!")
def recomendar():
    generos = [
        "ficção científica", "mistério", "aventura", "romance", "comédia"
    ]
    genero_escolhido = random.choice(generos)
    print(f"Recomendação de {genero_escolhido}:")
    if genero_escolhido == "ficção científica":
        print("Livro recomendado: 'Duna' de Frank Herbert")
        print("Filme recomendado: 'Blade Runner 2049'")
    elif genero_escolhido == "mistério":
        print("Livro recomendado: 'O Código Da Vinci' de Dan Brown")
        print("Filme recomendado: 'Garota Exemplar'")
    elif genero_escolhido == "aventura":
        print("Livro recomendado: 'As Aventuras de Huckleberry Finn' de Mark Twain")
        print("Filme recomendado: 'Indiana Jones e os Caçadores da Arca Perdida'")
    elif genero_escolhido == "romance":
        print("Livro recomendado: 'Orgulho e Preconceito' de Jane Austen")
        print("Filme recomendado: 'Simplesmente Acontece'")
    elif genero_escolhido == "comédia":
        print("Livro recomendado: 'O Guia do Mochileiro das Galáxias' de Douglas Adams")
        print("Filme recomendado: 'Debi & Lóide'")
    else:
        print("Desculpe, não tenho recomendações para esse gênero no momento.")
        recomendar()
def assistente():
    contexto = {}
    print(Fore.LIGHTBLUE_EX + "Olá Chefe! Eu sou Protus. Como posso ajudar você?")

    while True:
        try:
            comando = input(Fore.LIGHTMAGENTA_EX + "Você: ").lower()

            if "pesquisar" in comando:
                termo_pesquisa = comando.replace("pesquisar", "").strip()
                url_pesquisa = "https://www.google.com/search?q=" + termo_pesquisa
                print("Pesquisando por " + termo_pesquisa)
                abrir_navegador(url_pesquisa)
            elif "oi" in comando:
                print(Fore.LIGHTCYAN_EX + responder_saudacao())
            elif "estou bem" in comando:
                print(Fore.LIGHTCYAN_EX + "Que ótimo! Fico feliz em saber. Digite 'help' para acessar a lista de comandos do Protus ou 'suporte' para conversar com o desenvolvedor.")
            elif "como vai ?" in comando:
                print("Ótima; obrigado por perguntar, no que posso te ajudar hoje ?")
            elif "como vai?" in comando:
                print("muito bem e você ?")
            elif "bem também" in comando:
                print("que bom; no que posso ser útil ?")
            elif "péssimo" in comando:
                print("que pena, espero que melhores, no que posso ser útil ?")
            elif "bem" in comando:
                print("Que Ótimo! Como posso te dar um Help hoje ?")
            elif "o que faz ?" in comando:
                if "estado" in contexto and contexto["estado"] == "bem":
                    print("Converso com você e tento responder às suas perguntas.")
                else:
                    print("Eu sou a Protus o assistente virtual que foi designado para a missão de te ajudar.")
            elif "agradecimento" in comando:
                print(Fore.LIGHTCYAN_EX + responder_agradecimento())
            elif "trate um erro" in comando:
                print(Fore.LIGHTCYAN_EX + tratar_resposta_comando_nao_reconhecido())
            elif "modo calculadora" in comando:
                modo_calculadora()
            elif "busque por" in comando:
                termo_pesquisa = comando.replace("busque por", "").strip()
                buscar_wikipedia(termo_pesquisa)
            elif "conte uma piada" in comando:
                print("Preparando uma piada...")
                time.sleep(2)
                print(contar_piada())
            elif "notepad" in comando:
                print("Modo Bloco de Notas ativado. Digite seu texto. Para salvar, digite 'salvar'.")
                main()
            elif "criar poema" in comando:
                criar_poema()
            elif "suporte" in comando:
                print("criado em 07/06/2023 quarta feira, finalizado em 09/08/2023 quarta feira, atualizado pela ultima vez em 10/08/2023 quinta feira")
                time.sleep(3)
                print("desenvolvedor e programador : Vinícius Gabriel")
                print("contato : +5511942509143")
            elif "doar" in comando:
                numeros = "abcd12345"
                tamanho_chave = random.randint(6, 8)
                key = ''.join(random.choice(numeros) for _ in range(tamanho_chave))
                print("Aqui está sua chave privada:")
                time.sleep(2)
                print("ID:"+key)
                time.sleep(2)
                print("As chaves privadas ou ID são usados para ter certeza de que é humano, apenas um passo usado para verificar se és humano e não um tipo de IA, a chave pode ser usada também para ter certeza de que o pix foi feito por doadores que possuem a Protus IA ou que sejam apoiadores da coyoti.")
                printi = "por favor, escolha um desses valores e envie para o pix: gabnato500@gmail.com ;   valores :  10.00 R$        50.00 R$"
                print(printi)
                time.sleep(2)
                print("ou qualquer quantia.")
                time.sleep(1.5)
                print("na descrição do pix é obrigatório ter chave privada")

            elif "tudo bom?" in comando:
                sim = "Sim, melhor impossível"
                print(sim)
            elif "criar história" in comando:
                criar_historia()
            elif "criar senha segura" in comando:
                criar_senha_segura()
            elif "aprender programação" in comando:
                aprender_programacao()
            elif "recomendar livro ou filme" in comando:
                recomendar_livro_filme()
            elif "modo gpt" in comando:
                print("atenção: apenas um chat simples com um fluxo de conversa humanizada desenvolvido com o intuito de gerar engajamento, não é capaz de fazer pesquisas ou coisa assim, quando desejar encerrar basta digitar sair.")
                time.sleep(7)
                os.system('clear')
                with open('Protusgpt.py', 'r') as arquivo:
                    codigo = arquivo.read()
                    exec(codigo)
            elif "ping" in comando:
                def continuous_ping(host):
                    try:
                        count = 0
                        while True:
                            response_time = ping3.ping(host)
                            if response_time is not None:
                                count += 1
                                print(f"Response from {host}: time={response_time:.2f}ms - Pings sent: {count}")
                            else:
                                print(f"No response from {host} - Pings sent: {count}")
                            time.sleep(1)
                    except KeyboardInterrupt:
                        print("Ping stopped.")
                target_host = input("Enter the website or IP address to ping: ")
                continuous_ping(target_host)

            elif "clear" in comando:
                os.system('clear')
            elif "internet" in comando:
                os.system('netstat -r')
                print("aqui usamos o comando netstat -r, com ele você pode ver sua tabela de ip e conexão de rede")
                time.sleep(5)
                os.system('ip ntable')
                os.system('ip neigh show')
                print("mostrando a tabela para conexão IPv6 e IPv4")
                time.sleep(7)
                os.system('clear')
            elif "gerar html" in comando:
                    time.sleep(5)
                    os.system('clear')
                    with open('geradorHTML.py', 'r') as arquivo:
                        codigo = arquivo.read()
                        exec(codigo)
            elif "ver" in comando:
                    print("Aqui estão os comandos e funções disponíveis do Protus:")
                    print("- Pesquisar: Realiza uma pesquisa na web.")
                    print("- Abrir: Abre uma URL ou link.")
                    print("- Parar: Encerra a assistente.")
                    print("- Modo Calculadora: Ativa o modo calculadora.")
                    print("- Oi: Faz com que a maquina te pergunte como você está e gera um fluxo de conversa humanizada")
                    print("- Help: Exibe esta lista de comandos.")
                    print("- modo gpt: Use para fazer o protus ativar o modo chatbot, baseado no GPT apenas para conversas humanizadas.")
                    print("- Suporte: Exibe informações de contato do desenvolvedor.")
                    print("- Conte uma piada: Conta uma piada engraçada.")
                    print("- Notepad: Abre um bloco de notas para anotações.")
                    print("- Busque por: Realiza uma pesquisa na Wikipedia.")
                    print("- Criar poema: Cria um poema aleatório e inspirador")
                    print("- Criar história: Cria e exibe uma história aleatória de acordo com o gêneros escolhidos aleatoriamente")
                    print("- Criar senha segura: Cria uma senha ultra segura contra ataques de bruteforces, senha com até 12 caracteres")
                    print("- gerar html: Gera uma HTML simples e básica com fundo branco para o usuário, de acordo com o título que ele desejar e o conteúdo que ele adicionar")
                    print("- Aprender programação: Ajuda e auxilio para os iniciantes")
                    print("- Doar: doe valores de 10 a 50 reais ou qualquer outro valor que preferir, o dinheiro será gasto em investimentos para a coyoti e melhoria dos programas")
            elif "status" in comando:
                if __name__ == "__main__":
                    local_ip = get_local_ip()
                    ip_range = local_ip.rsplit('.', 1)[0] + '.'
                    
                    scanned_devices = scan_network(ip_range)
                    print("Dispositivos na rede:")
                    print("IP\t\t\tHostname")
                    print("-----------------------------------------")
                    for device in scanned_devices:
                        print(f"{device['ip']}\t\t{device['hostname']}")

            elif "sair" in comando:
                print("Até logo!")
            elif "contar piada" in comando:
                print("Olha, sinto muito em informar que o comando digitado não é valido e não existe, muito provavelmente isso foi um erro do meu desenvolvedor, tente usar o comando:  conte uma piada")
            elif "obrigado" in comando:
                responder_agradecimento()
            elif 'horas' in comando:
                hora = datetime.datetime.now().strftime('%H:%M')
                print('Neste momento são ' + hora)
            elif "help" in comando:
                    print("Aqui estão os comandos e funções disponíveis do Protus:")
                    print("- Pesquisar: Realiza uma pesquisa na web.")
                    print("- Abrir: Abre uma URL ou link.")
                    print("- Parar: Encerra a assistente.")
                    print("- Modo Calculadora: Ativa o modo calculadora.")
                    print("- Help: Exibe esta lista de comandos.")
                    print("- Suporte: Exibe informações de contato do desenvolvedor.")
                    print("- Ver: Dê uma olhada no que sou capaz de fazer")
                    print("- Clear: Use isso para Apagar o Histórico do terminal")
                    print("- Internet: Apenas use caso deseja ver algumas Informações sobre o IP e a conexão")
                    print("- Status: Exibe dispositivos na rede através do seu IP")
                    print("- Conte uma piada: Conta uma piada engraçada.")
                    print("- Notepad: Abre um bloco de notas para anotações.")
                    print("- Busque por: Realiza uma pesquisa na Wikipedia.")
                    print("- Criar poema: Cria um poema aleatório e inspirador")
                    print("- Criar história: Cria e exibe uma história aleatória de acordo com o gêneros escolhidos aleatoriamente")
                    print("- Criar senha segura: Cria uma senha ultra segura contra ataques de bruteforces, senhae com até 12 caracteres")
                    print("- Contar piada: Conta uma piada aleatória dentre uma lista extensa de  piadas")
                    print("- Aprender programação: Ajuda e auxilio para os iniciantes no E.L.P")
                    print("- Doar: doe valores de 10 a 50 reais ou qualquer outro valor que preferir, o dinheiro será gasto em materiais para o projeto elp e melhoria dos programas")
                    print("- modo gpt: Ativa o modo chatbot protus, baseado no chat GPT para conversas humanizadas.")
                    print("- Ping: Realiza disparos ping para um determinado host")
                    print("- gerar html: Gera uma HTML simples e básica com fundo branco para o usuário, de acordo com o título que ele desejar e o conteúdo que ele adicionar")
                    print(Fore.LIGHTRED_EX+"ATENÇÃO :")
                    print(Fore.LIGHTYELLOW_EX+"certifique-se de que ao escrever os comandos ou ao falar qualquer coisa com a protus, todas as letras estejam em minúsculo")
            else:
                print(tratar_resposta_comando_nao_reconhecido())

        except KeyboardInterrupt:
            print("\nAté logo!")
            break
        except Exception as e:
            print("Desculpe, não consegui interpretar.")
            print("Erro:", e)

if __name__ == "__main__":
    assistente()
