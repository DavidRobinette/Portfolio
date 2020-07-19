import sys
import os
from PIL import Image

image_folder = sys.argv[1]
after_edits_folder = sys.argv[2]


def folder_check(folder_path):
    check_folder = os.path.isdir(folder_path)

    if not check_folder:
        os.makedirs(folder_path)
        print('folder created for your files')

    else:
        print(folder_path, "folder already exists.")


# def image_processing(directory_path):
#     directory = directory_path
#     for file in os.listdir(directory):
#         image_name =file
#         if image_name.endswith('.jpg'):
#             image = Image.open(directory + '/' + image_name, mode='r')
#             image_name = image_name.replace('.jpg', '')
#             image.save(after_edits_folder + '/' + image_name + '.png')
#             continue
#         else:
#             continue
# one way of doing it
def image_processing(directory_path):
    directory = directory_path
    for file in os.listdir(directory):
        image_name = file
        if image_name.endswith('.jpg'):
            image = Image.open(directory + '/' + image_name, mode='r')
            image.save(after_edits_folder + '/' + image_name[0:image_name.rindex('.')] + '.png')
            continue
        else:
            continue


folder_check(after_edits_folder)
image_processing(image_folder)


