from app import app
from datetime import datetime

@app.route('/')
def home():
   return "hello world!"

@app.route('/hora')
def hora():
   return f"{datetime.now()}"

@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1, num2):
   return f"{int(num1 + num2)}"
