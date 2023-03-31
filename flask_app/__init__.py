from flask import Flask # import flask to create an instance
app = Flask(__name__) # cretae instance  of Flask named app
app.secret_key="do we even use session in this assignment?" # session will need secret key