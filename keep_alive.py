from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Ah, ha, ha, ha, stayin' alive, stayin' alive"

def run():
  app.run(host='192.168.100.119',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()