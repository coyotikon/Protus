import openai

# Substitua "SUA_API_KEY" pela sua chave de API
openai.api_key = "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"

def conversa_com_gpt(mensagem):
    conversa = []
    while True:
        mensagem_usuario = input("Usuário: ")
        if mensagem_usuario.lower() == "sair":
            break
        conversa.append({"role": "system", "content": "Você é um assistente de linguagem."})
        conversa.append({"role": "user", "content": mensagem_usuario})
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversa
        )
        mensagem_gpt = resposta["choices"][0]["message"]["content"]
        conversa.append({"role": "assistant", "content": mensagem_gpt})
        print("Assistente:", mensagem_gpt)

if __name__ == "__main__":
    print("Bem-vindo ao ChatGPT! Digite 'sair' para encerrar a conversa.")
    conversa_com_gpt("")
