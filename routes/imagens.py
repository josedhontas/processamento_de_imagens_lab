from flask import Blueprint, send_file
import os

imagens_bp = Blueprint('imagens', __name__)

@imagens_bp.route('/<int:imagem_id>')
def get_imagem(imagem_id):
    image_path = f'img\{imagem_id}.jpg'  #
    return send_file(image_path, mimetype='image/png')



