from flask import Flask, render_template,request,redirect,url_for
#il request servirà per mandare la richiesta all'utente redirect per reindirizzarlo correttamente e url_for servirà per il link

app = Flask(__name__)

Lista_Spesa = []

@app.route('/')
def home():
 return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 