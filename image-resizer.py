from PIL import Image
import glob
import os


# change path to your path or use current working directory without path
path = 'your_path'

# create list of paths to different images
# list of different image types/extensions (add extensions as needed)
img_types = ['*.JPG', '*.png']
images = []
for i in img_types:
    images.extend(glob.glob(f'{path}{i}'))

# create new folder
new_folder = f'{path}Resized_Images'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# resize images and save to new folder
for i in images:
    img = Image.open(i).resize((370, 370))
    img.save(f'{new_folder}/{os.path.split(i)[1]}')
