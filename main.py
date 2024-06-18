from openai import OpenAI
import datetime
import re

# Obter a data e hora atuais
current_time = datetime.datetime.now()
# Insira sua Key
client = OpenAI(
  api_key="")


solicitacao = str(input('Insira sua solicitação: '))

resultado = ''''''
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": '''
               Agora Você é programdo apenas para fazer código python. Ou seja você não dever retonar nada além de código python.
               
               '''},
              {"role":"user", "content": f"Apenas em códigos python, nada a mais: {solicitacao}"}
               ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        resultado += chunk.choices[0].delta.content

def excluir_conteudo(texto):
    # Define a regex para capturar tudo entre os delimitadores ```
    padrao = re.compile(r'```(.*?)```', re.DOTALL)
    
    # Encontra todas as ocorrências que correspondem ao padrão
    resultado = padrao.findall(texto)
    
    return ''.join(resultado)

resultado = resultado.replace("python","")

# Formatar a data e hora como string
timestamp = current_time.strftime("%d-%m-%y %H:%M:%S")

with open("log.txt", "a") as file:
    file.write("\n"+125*"_"+"\n"+timestamp+"\n"+solicitacao+"\n"+125*"-"+"\n")
    file.write("\n"+resultado+"\n")

resultado = excluir_conteudo(resultado)

exec(resultado)
