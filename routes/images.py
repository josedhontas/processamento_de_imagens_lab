from flask import Blueprint, send_file
from modules.images_processing_api import *
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

@images_bp.route('/gray/<int:image_id>')
def get_gray_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imreadgray(image_path)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

@images_bp.route('/histeq/<int:image_id>')
def get_histeq_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    img = histeq(img)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

@images_bp.route('/blur/<int:image_id>')
def get_blur_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    img = blur(img)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

@images_bp.route('/erode/<int:image_id>')
def get_erode_image(image_id):
    image_path = f'img/{image_id}.jpg'
    img = imread(image_path)
    element = seSquare3()
    img = erode(img, element)
    image = imshow(img)
    return send_file(image, mimetype='image/png')

