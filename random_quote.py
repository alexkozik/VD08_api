#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

#импортируем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной quote
def quote():
   quote = None
   if request.method == 'POST':
         quote = get_quote()
   return render_template("quote_bs.html", quote=quote)

#в функции прописываем город, который мы будем вводить в форме
def get_quote():
   #адрес, по которомы мы будем отправлять запрос
   url = "https://zenquotes.io/api/random"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

if __name__ == '__main__':
   app.run(debug=True)