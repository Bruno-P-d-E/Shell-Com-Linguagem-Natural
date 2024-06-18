# Shell-Com-Linguagem-Natural

## Projeto de Geração e Execução de Código Python com OpenAI

Este projeto utiliza a API da OpenAI para gerar e executar códigos Python com base em uma solicitação do usuário. Ele registra a solicitação e a resposta em um arquivo de log, e executa o código Python gerado após remover qualquer formatação desnecessária.

### Estrutura do Projeto

- **openai**: Biblioteca utilizada para interagir com a API da OpenAI.
- **datetime**: Biblioteca padrão do Python para manipulação de datas e horas.
- **re**: Biblioteca padrão do Python para manipulação de expressões regulares.

### Descrição do Código

1. **Obter a data e hora atuais:**
    ```python
    current_time = datetime.datetime.now()
    ```

2. **Inicialização do cliente da OpenAI:**
    ```python
    client = OpenAI(api_key="")
    ```

3. **Entrada do usuário:**
    ```python
    solicitacao = str(input('Insira sua solicitação: '))
    ```

4. **Criação da solicitação para a API da OpenAI:**
    ```python
    resultado = ''''''
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": '''
                   Agora Você é programado apenas para fazer código python. Ou seja você não deve retornar nada além de código python.
                   '''},
                  {"role":"user", "content": f"Apenas em códigos python, nada a mais: {solicitacao}"}
                   ],
        stream=True,
    )
    ```

5. **Construção do resultado a partir do stream:**
    ```python
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            resultado += chunk.choices[0].delta.content
    ```

6. **Função para excluir conteúdo não necessário:**
    ```python
    def excluir_conteudo(texto):
        # Define a regex para capturar tudo entre os delimitadores ```
        padrao = re.compile(r'```(.*?)```', re.DOTALL)
        
        # Encontra todas as ocorrências que correspondem ao padrão
        resultado = padrao.findall(texto)
        
        return ''.join(resultado)
    ```

7. **Remoção da palavra "python" do resultado:**
    ```python
    resultado = resultado.replace("python","")
    ```

8. **Formatação da data e hora como string:**
    ```python
    timestamp = current_time.strftime("%d-%m-%y %H:%M:%S")
    ```

9. **Registro da solicitação e resultado no arquivo de log:**
    ```python
    with open("log.txt", "a") as file:
        file.write("\n"+125*"_"+"\n"+timestamp+"\n"+solicitacao+"\n"+125*"-"+"\n")
        file.write("\n"+resultado+"\n")
    ```

10. **Remoção do conteúdo formatado do resultado:**
    ```python
    resultado = excluir_conteudo(resultado)
    ```

11. **Execução do código Python gerado:**
    ```python
    exec(resultado)
    ```

## Como Executar

1. **Configurar a API Key:**
    - Insira sua chave de API da OpenAI na inicialização do cliente:
      ```python
      client = OpenAI(api_key="SUA_API_KEY_AQUI")
      ```

2. **Executar o script:**
    - Rode o script em um ambiente Python:
      ```bash
      python seu_script.py
      ```

3. **Inserir a solicitação:**
    - Siga as instruções no terminal para inserir sua solicitação de código Python.

### Dependências

- `openai`
- `datetime` (padrão do Python)
- `re` (padrão do Python)

### Observações

- Este projeto é configurado para apenas gerar e executar códigos Python.
- Certifique-se de validar e sanitizar as entradas e saídas ao utilizar este script em um ambiente de produção para evitar execução de código malicioso.
