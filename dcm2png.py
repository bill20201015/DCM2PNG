import os

import cv2
import imageio
import numpy as np
import pydicom
from PIL import Image
import matplotlib.pyplot as plt

def get_names(path):
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dcm']:
                names.append(filename)

    return names


def convert_dcm_jpg(name):
    im = pydicom.dcmread('Database/' + name)

    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im, 0) / im.max()) * 255  # float pixels
    final_image = np.uint8(rescaled_image)  # integers pixels

    final_image = Image.fromarray(final_image)

    return final_image




#dcm_dir dcm 位置
#png_save_dir 图片保存位置
def dcm2png(dcm_dir, png_save_dir):

    dcm = pydicom.dcmread(dcm_dir)

    image = dcm.pixel_array

    plt.figure()
    plt.imshow(image, cmap=plt.cm.bone)
    plt.axis('off')
    plt.savefig(png_save_dir + '/fake_images-{}.png'.format(1))


