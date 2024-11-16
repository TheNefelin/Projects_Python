from gtts import gTTS #texto a voz
import speech_recognition as sr #voz a texto
import os # reproductor

r = sr.Recognizer()
txt = ""

with sr.Microphone() as source:
    print("Dí Algo...")
    audio = r.listen(source)

    try:
        txt = r.recognize_google(audio, language="es-us")
        print(txt)
    except:
        print("ERROR")

with open('leer.txt', 'w') as f:
    f.write(txt)

speech = gTTS(text = str(txt), lang = "es-us", slow = False)
speech.save("resp.mp3")
os.system("start resp.mp3")

# import openai

# api_key = "secret" 
# openai.api_key = api_key

# respuesta = openai.Completion.create(
#   engine="davinci",  # Otra opción de motor puede ser "curie"
#   prompt="¿Cuál es la capital de Francia?",
#   max_tokens=50,  
#   temperature=0.7  
# )

# print(respuesta.choices[0].text.strip())
