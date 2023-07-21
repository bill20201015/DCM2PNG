import os
import pydicom
import dicom2nifti
def convert_dicom_directory_to_nifti(dicom_dir, nifti_dir):
    # Ensure the output directory exists
    os.makedirs(nifti_dir, exist_ok=True)

    # Convert all DICOM files in the directory to NIfTI
    dicom2nifti.convert_directory(dicom_dir, nifti_dir)
# 输入和输出文件路径
dicom_directory = "C:\\Users\\shangkai\\Desktop\\123"
output_folder = "C:\\Users\\shangkai\\Desktop\\test"
dicom2nifti._is
convert_dicom_directory_to_nifti(dicom_directory, output_folder)

