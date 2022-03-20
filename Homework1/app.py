import binascii

from flask import *
from cryptography.fernet import *

app = Flask(__name__)
key = Fernet.generate_key()
cryptograph = Fernet(key)


@app.route('/')
def main_page():
    """
        This is main page of encryption and decryption website, that tells user about its capabilities

        :return:
        Web-site description string
    """
    return "It`s nothing interesting here, you should try out our encryption and decryption pages. Like " \
           "/encrypt?string='your message' or /decrypt?string='encryption token' "


@app.route('/encrypt')
def encryption_page():  # put application's code here
    """
        This is encryption page written with and for flask library. It's needed to encrypt text using python
        cryptography fernet library

        :return:
        String: "Encrypted result: <encryption_token>"
        """
    if not request.args.get('string'):
        return "Wrong syntax buddy, try to use ?string='your message' instead"
    else:
        token = cryptograph.encrypt(request.args.get('string').encode())
        return render_template("encryption.html", encryption_token=token.decode())


@app.route('/decrypt')
def decryption_page():
    """
        This is decryption page written with and for flask library. It's needed to decrypt text encrypted with python
        cryptography fernet library

        :return:
        String: "Decrypted result: <decrypted_text>"
    """
    if not request.args.get('string'):
        return "Wrong syntax buddy, try to use ?string='encryption token' instead"
    else:
        try:
            text = cryptograph.decrypt(request.args.get('string').encode())
            return render_template("decryption.html", decrypted_text=text.decode())
        except InvalidToken:
            return "Looks like it`s not our token or you`ve lost some symbols"


@app.route('/<name>')
def missing_page(name):
    """
        This is missing page of encryption and decryption website, that tells user that page he`s trying
        to access is missing and he should try another one

        :param name:
        Every missing website page

        :return:
        Help string
    """
    if name:
        return "We don`t have such page still, try to use: /encrypt?string='your " \
               "message' or /decrypt?string='encryption token'"


if __name__ == '__main__':
    app.run()
