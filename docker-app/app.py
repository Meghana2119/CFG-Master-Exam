from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    html = """
    <html>
        <head>
            <title>CFG Test WebPage</title>
        </head>
        <style>
            body {
                background-image: url('https://scx1.b-cdn.net/csz/news/800/2017/theoreticala.jpg');
                color: #FFFFFF;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-size: cover;
                font-family: Roboto, Arial, Calibri;
                
            }
        </style>
        <body>
            <h1>Hosting Docker App with AWS - CFG TEST</h1>
            <p>Student: "YOUR NAME", "YOUR SURNAME"</p>
        </body>
    </html>
    """
    return html
                                      

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
