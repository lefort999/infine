from flask import Flask
der = Flask(__name__)
@der.route('/')
def home():
    return "bienvenue"
if __name__ == '__main__':    
    der.run(debug=True)