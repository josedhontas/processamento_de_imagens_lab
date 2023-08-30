from flask import Blueprint, send_file
from module.bilioteca import *
import os

# Importe as funções necessárias aqui (imread, contrast, imshow)

images_bp = Blueprint('images', __name__)

@images_bp.route('/<int:image_id>')
def get_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    #img = negative(img)
    #img = contrast(img, 10, 10)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

@images_bp.route('/negative/<int:image_id>')
def get_negative_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    img = negative(img)
    #img = contrast(img, 10, 10)
    image = imshow(img)
    return send_file(image, mimetype='image/png')
