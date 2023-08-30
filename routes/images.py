from flask import Blueprint, send_file
from module.bilioteca import *
import os

images_bp = Blueprint('images', __name__)

@images_bp.route('/<int:image_id>')
def get_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

@images_bp.route('/negative/<int:image_id>')
def get_negative_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    img = negative(img)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

@images_bp.route('/thresh/<int:image_id>')
def get_thresh_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    img = thresh(img, 40)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

