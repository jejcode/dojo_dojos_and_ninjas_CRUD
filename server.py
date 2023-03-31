from flask_app import app # import Flask instance
#import controllers
from flask_app.controllers import dojos
from flask_app.controllers import ninjas



if __name__ == '__main__':
    app.run(debug = True, port = 8000)