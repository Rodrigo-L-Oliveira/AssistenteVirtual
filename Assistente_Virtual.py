import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executar_comandos():
    comando = ''
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google_cloud(voz, language='pt-BR')
            comando = comando.lower()
            if 'Pudim' in comando:
                comando = comando.replace('Pudim', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('O microfone não está funcionando')
    return comando

def comandos_voz_usuario():
    while True:
        comando = executar_comandos()

        if 'que horas são' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            maquina.say('Agora são' + hora)
            maquina.runAndWait()

        elif 'procure por' in comando:
            procurar = comando.replace('procure por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            maquina.say(resultado)
            maquina.runAndWait()

        elif 'toque' in comando:
            musica = comando.replace('toque', '')
            resultado = pywhatkit.playonyt(musica)
            maquina.say('Tocando música')
            maquina.runAndWait()

        elif 'sair' in comando:
            break

def comandos_texto_usuario():
    while True:
        comando = input('Digite um comando: ')

        if 'que horas são' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            print('Agora são' + hora)

        elif 'procure por' in comando:
            procurar = comando.replace('procure por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            print(resultado)

        elif 'toque' in comando:
            musica = comando.replace('toque', '')
            print('Desculpe, não posso tocar música no modo de texto.')

        elif 'sair' in comando:
            break

modo = input('Você gostaria de se comunicar por voz ou por texto? ')
if modo.lower() == 'voz':
    comandos_voz_usuario()
elif modo.lower() == 'texto':
    comandos_texto_usuario()
else:
    print('Modo desconhecido. Por favor, escolha "voz" ou "texto".')
