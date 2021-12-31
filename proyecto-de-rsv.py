import speech_recognition as sr
import subprocess as sub
import pyautogui as auto
import pyttsx3 as voz
from time import sleep
import sounddevice as sd
from scipy.io.wavfile import write
import webbrowser as web

def interpretar(comando_de_audio):
    comando_de_audio = comando_de_audio.split(' ')
    
    ver_video = ('video') in comando_de_audio
    escribir = ('escribir') in comando_de_audio
    musica = ('audio') in comando_de_audio
    compras = ('compras') in comando_de_audio
    buscar = ('Buscar') in comando_de_audio

    if ver_video is True:
        abrir_yotube()

    elif escribir is True:
        abrir_bloc_de_notas()

    elif  musica is True:
        abrir_spoty()

    elif compras is True:
        abrir_amazon()
        
    elif buscar is True:
        abrir_google()
    else:
        
        print('La funcion no esta definida')


        
def abrir_bloc_de_notas():
    sub.call('start notepad.exe', shell=True)
    sleep(1.5)
    auto.write('Estoy listo para escribir tu texto')

    Computadora = voz.init()
    velocidad = Computadora.getProperty('rate')
    Computadora.setProperty('rate',velocidad-25)

    # Colocamos la voz con acento mexicano
    Computadora.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    Computadora.say('Estoy lista para escribir el texto')
    Computadora.runAndWait()

def abrir_yotube():
    Computadora = voz.init()
    velocidad = Computadora.getProperty('rate')
    Computadora.setProperty('rate',velocidad-25)

    Computadora.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    Computadora.say('Abriendo Youtube')
    Computadora.runAndWait()
    web.open('https://www.youtube.com/',1,True)


def abrir_spoty():
    Computadora = voz.init()
    velocidad = Computadora.getProperty('rate')
    Computadora.setProperty('rate',velocidad-25)

    Computadora.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    Computadora.say('Abriendo spotify')
    Computadora.runAndWait()
    sub.call([r'C:/Users/fst_9/AppData/Roaming/Spotify/Spotify.exe'])
    sleep(1.5)

def abrir_amazon():
    Computadora = voz.init()
    velocidad = Computadora.getProperty('rate')
    Computadora.setProperty('rate',velocidad - 25)

    Computadora.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    Computadora.say('Abriendo Amazon')
    Computadora.runAndWait()
    web.open('https://www.amazon.com.mx/',1,True)


def abrir_google():
    Computadora = voz.init()
    velocidad = Computadora.getProperty('rate')
    Computadora.setProperty('rate',velocidad - 25)

    
    Computadora.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    Computadora.say('Abriendo Google')
    Computadora.runAndWait()
    web.open('https://www.google.com.mx/',1,True)

print("""
    -Programa beta de la aplicacion-

        Comandos que tengo:
            video   - Abro Youtube
            escribir- Abro bloc de notas
            compras - Abro amazon
            audio   - Abro spotify
            buscar  - Abro google

    Programa desarrollado por Fernando Sosa T.
""")
# Escuchar el audio con el micronfono de la computadora
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Dicta la orden...')
    audio = r.listen(source)
    # Si se entendio el audio
try:
    comando = r.recognize_google(audio, language='es-MX')
    print('Creo que dijiste: '+ comando)
    interpretar(comando)

    # Si no se entendio
except sr.UnknownValueError:
    print('No te he entendido')

    # Si no se tiene conexion a internet o al servicio de google
except sr.RequestError as e:
    print('No pude establecer la conexión;{0}'.format(e))
