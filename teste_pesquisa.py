"""from googlesearch import search

row = b'\ud800'.decode('utf8','replace')


ip = input("What would you like to search for? ")


for url in search(row(ip), stop=5):
     print(url)"""
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from random import choice
import speech_recognition as sr
import pyttsx3
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyowm
import requests as rq
import webbrowser as web
import time
import os
import sys
from googlesearch import search

reproducao = pyttsx3.init('sapi5')


def sai_som(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as s:
     r.adjust_for_ambient_noise(s)
                    
        
        
     print('O que deseja pesquisar: ')
     sai_som('O que deseja pesquisar ')
     while True: 
          audio1 = r.listen(s)
          speech1 = r.recognize_google(audio1, language='pt').lower()   
          url1 = ('https://www.google.com.br/search?q=')
          pronta = (url1 + speech1)
          if "acabou a pesquisa" in speech1:
               break
          if "vídeos no youtube" in speech1 or "videos no youtube" in speech1:               
               url1 = ('https://www.youtube.com/results?q=')
               
          
          if "brainli" in speech1 or "brainly" in speech1:
               url1 = ('https://brainly.com.br/app/ask?entry=hero&q=')
          
          elif sr.UnknownValueError:                
               sai_som("Hm")
               
          print("EU: ", speech1)
          
            
          web.open(pronta)







