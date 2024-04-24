# import modules
from pathlib import Path
from PIL import Image

# load images
directory = 'images'
image_files = Path(directory).glob('*.jpg')
count = 0
for image_file in image_files:
    image = Image.open(image_file)
    # image = Image.open('images/0603170325589_00_678029bbc55011a335aa0623a5fbd863.jpg')
    # resize images to 200 wide by 333 height
    resized = image.resize((200,333))
    # rename images
    img_file = str(image_file)
    img_no = img_file[img_file.find('_')+1: img_file.find('_')+3]
    new_name = './processed/c' + str(img_no) + '.jpg'
    # save renamed, resized images
    resized.save((new_name))
    count += 1
    
# save images
print('renamed '+str(count)+ 'files')
#resized.show()