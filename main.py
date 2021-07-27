from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from random import choice
import speech_recognition as sr
import pyttsx3
from configuracoes import *
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyowm
import requests as rq
import webbrowser as web
import time
import os
import sys
from googlesearch import search





version = "1.4.0"

caminho_navegador = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
reproducao = pyttsx3.init('sapi5')
voices = reproducao.getProperty('voices')
reproducao.setProperty('voice', voices[0].id)
r = sr.Recognizer()

chatbot = ChatBot("Rafinha",
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                database_uri='sqlite:///database.db')



lista_erros = [
    "Não entendi o que você disse",
    "Por favor repita novamente",
    "Sua fala ficou confusa em minha cabeça, por favor repita",
    "Repita novamente por favor",
    "Fale com a boca mais aberta para maior compreenção"
]
resposta_erro_aleatoria = choice(lista_erros)
lista_musica = [
    "(Música - Ela Tá Querendo Namorar) Saveiro brasil 8.mp3",
    "DJ GBR - Quando você se foi chorei (Clipe Oficial).mp3",
    "DJ GBR - RAVE DAS FAVELAS 4 (LANÇAMENTO 2020).mp3",
    "DJ GBR - RAVE PUMP IT - TOMA TOMA (LANÇAMENTO 2020).mp3",
    "Infect Drop - Noites Em Claro (Original Mix).mp3",
    "MC ANJIM - AGUA ROSA - DJ PH DA SERRA E DJ WJ DA INESTAN (CLIPE OFICIAL) Doug FIlmes Hits.mp3",
    "MC Don Juan - Te Prometo (Official Audio) Dennis DJ.mp3",
    "MC Jottapê, MC Kekel e Kevinho - Eterna Sacanagem  (kondzilla.com).mp3",
    "MC MANEIRINHO - TU VAI MAMAR DEPOIS DO BAILE NA HIDROMASSAGEM, CLIMA DE BOATE ( DJ JR E IAN GIRÃO ).mp3",
    "MC POZE - TO VOANDO ALTO  [ DJ GABRIEL DO BOREL ] OFICIAL.mp3",
    "MC YSA - BAILE DA COLÔMBIA - CLIPE OFICIAL.mp3"
]
lista_netflix_acao = [
    "https://www.netflix.com/watch/80134513?trackId=253863245&tctx=1%2C3%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771730X19XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80011010?trackId=253863245&tctx=1%2C5%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771730X19XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80027980?trackId=253863245&tctx=1%2C2%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771730X19XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80158583?trackId=253788158&tctx=3%2C1%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771732X54XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80031634?trackId=253863245&tctx=1%2C1%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771730X19XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80091595?trackId=253863245&tctx=1%2C4%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771730X19XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80071048?trackId=251128852&tctx=2%2C2%2C7c3dc4c6-90de-42ec-b990-1517f34a39fd-73586761%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_14562786X3XX1583434405335%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80164399?trackId=253788158&tctx=3%2C3%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771732X54XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/80192187?trackId=253788158&tctx=3%2C4%2C2592be3d-ea67-47cd-9ad3-cab647ece007-73355295%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771732X54XX1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/70098610?trackId=253436797&tctx=6%2C1%2C7c3dc4c6-90de-42ec-b990-1517f34a39fd-72934830%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771735X29X80150243X1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/60020801?trackId=251148981&tctx=8%2C5%2C7c3dc4c6-90de-42ec-b990-1517f34a39fd-72934830%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771737X28X5824X1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT",
    "https://www.netflix.com/watch/70251669?trackId=253882154&tctx=9%2C5%2C7c3dc4c6-90de-42ec-b990-1517f34a39fd-72934830%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_13771738X28X2125X1583433895137%2C4b2d6ac8-0bec-4553-bbf2-fe6aa6b4104c_ROOT"           
]
lista_netflix_comedia = [
    "https://www.netflix.com/watch/80018689?trackId=253863245&tctx=1%2C3%2Ca9198986-7794-4598-b7cf-7d747a6b1e18-75087030%2C6194066c-6a75-4719-929f-f2ad32fffb8b_57866891X19XX1583434910331%2C6194066c-6a75-4719-929f-f2ad32fffb8b_ROOT",
    "https://www.netflix.com/watch/81209203?trackId=251132817&tctx=0%2C0%2C76eac300-9f1a-4829-9b20-b6bc203882ac-5437609%2C6194066c-6a75-4719-929f-f2ad32fffb8b_57866894X28X51056X1583434910331%2C6194066c-6a75-4719-929f-f2ad32fffb8b_ROOT",
    "https://www.netflix.com/watch/80098100?trackId=253754081&tctx=5%2C0%2Cd410760b-13c9-4672-abb6-7a6816753b76-74692371%2C6194066c-6a75-4719-929f-f2ad32fffb8b_57866895X28X1402X1583434910331%2C6194066c-6a75-4719-929f-f2ad32fffb8b_ROOT",
    "https://www.netflix.com/watch/60034587?trackId=253863245&tctx=1%2C5%2Ca9198986-7794-4598-b7cf-7d747a6b1e18-75087030%2C6194066c-6a75-4719-929f-f2ad32fffb8b_57866891X19XX1583434910331%2C6194066c-6a75-4719-929f-f2ad32fffb8b_ROOT"    
]

#DEF's = Funções...
def intro():
    msg = "Assistente - version {} /by: Rafael Melo".format(version)
    print("-" * len(msg) + "\n{}\n".format(msg) + "-" * len(msg))

def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

def temperatura_catalao():
    own = pyowm.OWM('3800a8f169347bb2a9f75f081c3d367e')
    observation = own.weather_at_place('Catalão, BR')
    weather = observation.get_weather()
    temperatura = weather.get_temperature('celsius')['temp']

    print(temperatura)
    sai_som("A temperatura média de catalão é de {} graus Celsius.".format(temperatura))

def abrir(speech):
    try:
        if "google" in speech:
            web.open("https://www.google.com/")
            sai_som ("abrindo google...")
        elif "facebook" in speech:
            web.open("https://www.facebook.com/")
            sai_som ("abrindo facebook...")
        elif "youyube" in speech:
            web.open("https://www.youtube.com/?gl=BR")
            sai_som("abrindo youtube...")        
        
        else:
            sai_som ("Site não cadastrado para aberturas")
                       
    except:
        sai_som ("Houve um erro")

def pesquisar(speech):
    with sr.Microphone() as s:
        
        print('O que deseja pesquisar: ')
        sai_som('O que deseja pesquisar ')
        
        r.adjust_for_ambient_noise(s)                    
                        
        while True: 
            audio1 = r.listen(s)
            speech1 = r.recognize_google(audio1, language='pt').lower()   
            url1 = ('https://www.google.com.br/search?q=')
            if "finalizar pesquisa" in speech1:
                break
            if "vídeos no youtube" in speech1 or "videos no youtube" in speech1:
                url1 = ('https://www.youtube.com/results?q=')
            if "brainli" in speech1 or "brainly" in speech1:
               url1 = ('https://brainly.com.br/app/ask?entry=hero&q=')
            
            elif sr.UnknownValueError:                
                sai_som("Hm")
            print("EU: ", speech1)
            
            pronta = (url1 + speech1)
            
            web.open(pronta)
            
            while sr.UnknownValueError:
                #time.sleep(3)
                #sai_som(resposta_erro_aleatoria)
                break
            
    
    
        
   
     




#treinando
def treinamento():
    trainer = ChatterBotCorpusTrainer(chatbot)

    trainer.train(
        "chatterbot.corpus.portuguese"
    )


def assistente():
    sai_som("Quando eu falo algo, você deve esperar 2 segundos para responder")
    sai_som("Contando agora, daqui 2 segundos estou te escutando, pode falar")
    while True:
        
        with sr.Microphone() as s:
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
            speech = r.recognize_google(audio, language='pt').lower()
            while 'catarina' in speech:                                       
                cgtr = chatbot.get_response(speech)
                                                   
                if 'pesquisa' in speech:
                    print("EU: ", speech)
                    pesquisar(speech)
                    response = ("Sua pesquisa acabou")  
                            
                elif "qual é" in speech or "seu nome" in speech:                
                    print("EU: ", speech)
                    response = ("Joaninha, {}".format(cgtr))
                                                            
                elif "temperatura" in speech or  "Catalão" in speech:
                    print("EU: ", speech)
                    response = temperatura_catalao()
                    
                elif "internet" in speech or "navegador" in speech:
                    print("EU: ", speech)
                    response = abrir(speech) 
                              
                elif "bloco de notas" in speech:
                    print("EU: ", speech)
                    sai_som ("abrindo bloco de notas")
                    response = os.startfile('Notepad.exe')
                    
                elif "filme" in speech:
                    if "ação" in speech:                                            
                        print("EU: ", speech)
                        response = web.open(choice(lista_netflix_acao), autoraise=True)                        
                        sai_som("Abrindo filme de ação.")
                        
                                            
                elif "comédia" in speech:
                    print("EU: ", speech)
                    response = web.open(choice(lista_netflix_comedia), autoraise=True)                        
                    sai_som("Abrindo filme de comédia.")
                                       
                elif "fechar assistente" in speech:
                    print("EU: ", speech)
                    sai_som("Até uma outra hora, bye bye")
                    os._exit(0)
                elif "calculadora" in speech:
                    print("EU: ", speech)  
                    sai_som("abrindo calculadora")
                    response = os.startfile('calc.exe')
                    
                                                
                else:        
                    response = cgtr                                                       
                    print("EU: ", speech)
                    print(response)    
                    sai_som(response)
                    
                                       
           
        
            while sr.UnknownValueError:
                #time.sleep(3)
                #sai_som(resposta_erro_aleatoria)
                continue
        
            while (KeyboardInterrupt, EOFError, SystemExit):        
                continue
            while (KeyError):
                print("Joaninha: ", "Não entendi o que você disse.")
                sai_som("Não entendi o que você disse.")
                continue
            

if __name__ == '__main__':
    #treinamento()
    intro()
    sai_som("Iniciando")
    assistente()
            
