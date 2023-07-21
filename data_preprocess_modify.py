# import pydicom
import numpy as np
# import cv2
import os
# import matplotlib.pyplot as plt
# import matplotlib.image as mping
# import shutil
import glob
import PIL
from PIL import Image
from PIL import ImageOps


dataProcessing = os.listdir('./bmp_latest_with_modification')

# print(image_folders)

for image_folders in dataProcessing:
    # 将1_01_P等文件解析 如果不是文件夹则跳过
    if len(image_folders) != 6:
        continue
    print(image_folders)
    image_sub_folders = os.listdir(os.path.join('./bmp_latest_with_modification', image_folders))
    if not os.path.isdir(os.path.join('./bmp_latest_with_modification', image_folders, 'CT_modified')):
        os.mkdir(os.path.join('./bmp_latest_with_modification', image_folders, 'CT_modified'))
    if not os.path.isdir(os.path.join('./bmp_latest_with_modification', image_folders, 'MR_modified')):
        os.mkdir(os.path.join('./bmp_latest_with_modification', image_folders, 'MR_modified'))


    for image_sub_folder in image_sub_folders:
        # print('yes.')
        # print(len(image_sub_folder))
        if len(image_sub_folder) != 2:
            continue
        # print('ok.')
        print(image_sub_folder)
        if image_sub_folder[0:2] == 'CT':
            print('yes')
            filenames_CT = os.listdir(os.path.join('./bmp_latest_with_modification', image_folders, image_sub_folder))
            # filenames_CT.sort(key=lambda x: int(x[:-4]))
            filenames_CT.sort(key=lambda x: int(x.split('.')[-2]))
            index = 0
            for filename_CT in filenames_CT:
                img_ct = Image.open(os.path.join('./bmp_latest_with_modification', image_folders, image_sub_folder, filename_CT)).convert('RGB')
                ivt_image_ct = ImageOps.invert(img_ct)
                bbox_ct = ivt_image_ct.getbbox()
                crop_img_ct = img_ct.crop([bbox_ct[0], bbox_ct[1], bbox_ct[2], bbox_ct[3]])
                crop_img_resize_ct = crop_img_ct.resize((512, 512))
                new_ct = 'CT' + '_' + image_folders[0:6] + '_' + (str(index)).zfill(6) + '.png'
                dst_ct = os.path.join('./bmp_latest_with_modification', image_folders, "CT_modified", new_ct)
                crop_img_resize_ct.save(dst_ct, format='PNG')
                index += 1


        if image_sub_folder[0:2] == 'MR':
            filenames_MR = os.listdir(os.path.join('./bmp_latest_with_modification', image_folders, image_sub_folder))
            index = 0
            for filename_MR in filenames_MR:
                img_mr = Image.open(os.path.join('./bmp_latest_with_modification', image_folders, image_sub_folder, filename_MR)).convert('RGB')
                ivt_image_mr = ImageOps.invert(img_mr)
                bbox_mr = ivt_image_mr.getbbox()
                crop_img_mr = img_mr.crop([bbox_mr[0], bbox_mr[1], bbox_mr[2], bbox_mr[3]])
                crop_img_resize_mr = crop_img_mr.resize((512, 512))
                new_mr = 'MR' + '_' + image_folders[0:6] + '_' + (str(index)).zfill(6) + '.png'
                dst_mr = os.path.join('./bmp_latest_with_modification', image_folders, "MR_modified", new_mr)
                crop_img_resize_mr.save(dst_mr, format='PNG')
                index += 1

