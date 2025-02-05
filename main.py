import pyttsx3

# Inicializa o engine de voz
engine = pyttsx3.init()

# Configura a voz (opcional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Escolhe a primeira voz disponível
engine.setProperty('rate', 200)  # Ajusta a velocidade da fala

# Lê o texto do arquivo
with open("texto.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Converte o texto em fala
engine.say(texto)
engine.runAndWait()
