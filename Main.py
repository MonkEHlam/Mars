from flask import Flask
from flask import url_for
app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion_image')
def red_planet():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась"
                    style="width:25%">
                    </br> 
                    <div class="alert alert-warning" role="alert">
                        Человечество вырастает из детства.
                    </div>
                        <div class="alert alert-dark" role="alert">
                        Человечеству мала одна планета.
                    </div>
                        <div class="alert alert-danger" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                        <div class="alert alert-warning" role="alert">
                        И начнем с Марса!"
                    </div>
                        <div class="alert alert-dark" role="alert">
                        "Присоединяйся!"
                    </div>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')