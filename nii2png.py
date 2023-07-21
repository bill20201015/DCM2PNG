import warnings

import os  # 遍历文件夹
import nibabel as nib  # nii格式一般都会用到这个包
import imageio  # 转换成图像
from PIL import Image
from skimage.transform import resize


def nii_to_image(folder):
    filepath = folder   # 存取nii文件的文件夹
    filenames = os.listdir(filepath)

    imgfile = folder  # 存取png图片的文件夹
    if not os.path.exists(imgfile):
        os.mkdir(imgfile)

    print(filenames)
    slice_trans = []

    for f in filenames:  # 开始读取nii文件
        s = f[-3:]
        print(s)

        if s != '.gz':
            continue
        s1 = f[:-4]
        print(s1)
        imgfile_path = imgfile + s1
        print("imgfile_path:" + imgfile_path)
        img_path = os.path.join(filepath, f)
        img = nib.load(img_path)  # 读取nii

        print("img:")
        print(img)
        img_fdata = img.get_fdata()

        fname = f.replace('.nii', '')  # 去掉nii的后缀名
        # fname = folder[4:6] + "_"+fname
        img_f_path = os.path.join(imgfile, fname)
        if not os.path.exists(img_f_path):
            os.mkdir(img_f_path)

        # 创建nii对应的图像的文件夹
        # # if not os.path.exists(img_f_path):
        # os.mkdir(img_f_path) #新建文件夹
        # #开始转换为图像
        if '.gz' in s1:
            (x, y, z, _) = img.shape
            print("img2:")
            print(img.shape)
        else:
            (x, y, z) = img.shape
            print("img3:")
            print(img.shape)

        for i in range(z):  # z是图像的序列
            silce = img_fdata[:, :, i]  # 选择哪个方向的切片都可以
            # silce = img_fdata[:, i, :]  # 选择哪个方向的切片都可以
            # silce = img_fdata[i, :, :]  # 选择哪个方向的切片都可以
            # silce = (silce * 255.0).astype('unit8')
            # print
            # slice = silce.astype(np.uint8)
            silce = resize(silce, (256, 256))
            imageio.imwrite(os.path.join(img_f_path, '{}_axial_{}.png'.format(fname[:-3], i)), silce)
            img = Image.open(os.path.join(img_f_path, '{}_axial_{}.png'.format(fname[:-3], i)))

            img.save(os.path.join(img_f_path, '{}_axial_{}.png'.format(fname[:-3], i)))
    return 0


if __name__ == '__main__':
    filePath = "C:\\Users\\shangkai\\Desktop\\test"
    nii_to_image(filePath)

