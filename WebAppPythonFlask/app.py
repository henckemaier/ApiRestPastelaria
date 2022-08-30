from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola_mundo():
        return "<h1>Olá Mundo!<br>Eduardo Henckemaier Borguesan</h1>", 200

if __name__ == "__main__":
        app.run()