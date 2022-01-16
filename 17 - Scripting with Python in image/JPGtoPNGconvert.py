import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    imp = Image.open(f'{image_folder}{filename}')
    clean_name=os.path.splitext(filename)[0]
    imp.save(f'{output_folder}{clean_name}.png','png')
    print('All done')