from flask import Blueprint, send_file
from module.bilioteca import *
import os

# Importe as funções necessárias aqui (imread, contrast, imshow)

imagens_bp = Blueprint('imagens', __name__)

@imagens_bp.route('/<int:imagem_id>')
def get_imagem(imagem_id):
    image_path = f'img/{imagem_id}.jpg'
    img = imread(image_path)
    img = contrast(img, 10, 10)

    # Gerar a imagem usando imshow
    imagem = imshow(img)

    # Retornar a imagem como resposta
    return send_file(imagem, mimetype='image/png')
