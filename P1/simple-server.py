
from flask import Flask

SECRET_MESSAGE = "Secret Message"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE

if __name__ == "__main__":
    #Please check whether the key and cert names are correct
    app.run(port=4567, ssl_context=( 'signed-server-public-key.pem', 'server-private-key.key') )  #ssl_context=('cert.crt', 'key.pem'))
