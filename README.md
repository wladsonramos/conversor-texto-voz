# Conversor de Texto para Voz em Python

Este é um simples projeto em Python que converte texto em fala (voz) utilizando a biblioteca pyttsx3. O programa lê o conteúdo de um arquivo de texto (.txt) e o converte em áudio, utilizando o mecanismo de síntese de fala do sistema.

# Funcionalidades

- Lê o texto de um arquivo .txt.
- Converte o texto lido em fala usando o motor pyttsx3.
- Permite ajustar a velocidade da fala e escolher a voz (se disponível no sistema).

# Tecnologias Usadas

- Python 3.x: Linguagem utilizada para o desenvolvimento do projeto.
- pyttsx3: Biblioteca para conversão de texto para fala, que funciona de forma offline.

# Como Rodar o Projeto

**1. Pré-requisitos**
  - **Python 3.x** instalado no seu sistema.
  - O módulo pyttsx3 precisa ser instalado. Se ainda não tiver o módulo, basta rodar o seguinte comando:

```
pip install pyttsx3
```

**2. Como Usar**

1. Crie um arquivo chamado texto.txt no mesmo diretório do script main.py.
2. Adicione o texto que deseja que seja convertido em fala dentro deste arquivo.
3. Execute o script Python:

```
python main.py
```

O script irá ler o conteúdo do arquivo texto.txt e convertê-lo em fala. O áudio será reproduzido imediatamente.

**3. Personalização**

- Para ajustar a velocidade da fala, modifique o valor da propriedade rate na linha:

```
engine.setProperty('rate', 200)  # Aumente ou diminua o número conforme necessário
```

- Para mudar a voz, altere a linha que configura a voz:

```
engine.setProperty('voice', voices[0].id)  # Escolha o índice da voz desejada
```

# Contribuição

Sinta-se à vontade para contribuir com melhorias neste projeto! Se encontrar algum erro ou tiver sugestões, crie uma issue ou envie um pull request.
