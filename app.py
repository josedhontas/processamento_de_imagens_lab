from flask import Flask
from routes.images import images_bp

app = Flask(__name__)

app.register_blueprint(images_bp, url_prefix='/images')

@app.route('/')
def home():
    return 'Processamento de imagens'

if __name__ == '__main__':
    app.run()
