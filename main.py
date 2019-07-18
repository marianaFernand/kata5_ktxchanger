from tkinter import *
from tkinter import ttk


import configparser
import json
import requests

config = configparser.ConfigParser()
config.read("config.ini")

inSymbol = input ("qué moneda quieres convertir: ")
outSymbol = input ("en qué otra moneda: ")

url = config["fixer.io"]["RATE_LATEST_EP"]
api_key = config["fixer.io"]["API_KEY"]

url = url.format(api_key, inSymbol, outSymbol)
response = requests.get(url)
if response.status_code ==200:
    print (response.text)
else:
    print ("se ha producido un error en la petición", response.status_code)



