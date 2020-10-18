import substructure
from random import choice
import speak
import datetime
import selenium
import time
import webbrowser
import random
import os
import sys
from os import system
import requests
from random import choice
import json
import urllib.request
import html
from bs4 import BeautifulSoup
import lxml.html

def program(self):
    kelimeler = substructure.molds(self)[2]
    voice = substructure.search_algorithm(self)

    meraba = kelimeler[0]
    nasılsın = kelimeler[1]
    iyiyim = kelimeler[4]
    nasıl_gidiyor = kelimeler[2]
    ukalalık = kelimeler[5]


    if voice in meraba:
        voice = choice(meraba)
        return voice
    if voice in nasılsın:
        voice = choice(['im fine', 'fine', 'thanks'])
        return voice
    if voice in iyiyim and 'you' in voice:
        voice = choice(iyiyim)
        return voice
    if voice in iyiyim and 'you' not in voice:
        voice = choice('great')
        return voice
    if voice in nasıl_gidiyor:
        voice = choice(['nothink', 'not bad', 'it cloud be better'])
        return voice
    if voice in ukalalık:
        voice = choice(['an answer, for me', 'i know, but you teached me just for a litle dialog'])
        return voice

speak(program('hello how are you'))