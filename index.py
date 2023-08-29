from flask import Flask
from routes.imagens import imagens_bp

app = Flask(__name__)

app.register_blueprint(imagens_bp, url_prefix='/imagens')

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
