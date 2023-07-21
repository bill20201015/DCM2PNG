# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
import dcm2png

if __name__ == '__main__':
    dcm_dir = "C:\\Users\\shangkai\\Desktop\\LIDC-IDRI_1-50\\LIDC-IDRI-0001\\1.3.6.1.4.1.14519.5.2.1.6279.6001.175012972118199124641098335511\\1.3.6.1.4.1.14519.5.2.1.6279.6001.141365756818074696859567662357\\000001.dcm"
    png_save_dir = "C:\\Users\\shangkai\\Desktop\\test"
    dcm2png.dcm2png(dcm_dir, png_save_dir)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
