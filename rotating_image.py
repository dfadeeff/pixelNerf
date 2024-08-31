import os
import imageio
from PIL import Image


# Base directory containing the images
#images_dir  = 'eval_out/cars_sofa/000_4d3bf8ef55b4e4fcdb66736e6592e424'  # Update with the correct path
#images_dir  = 'src/data/NMR_Dataset/000/4d3bf8ef55b4e4fcdb66736e6592e424/image'  # Update with the correct path
images_dir  = 'src/data/chairs_test/1ee92a9d78cccbda98d2e7dbe701ca48/rgb'  # Update with the correct path
output_file = os.path.join(images_dir, 'rotating_object.gif')

# Get all image files in the directory
image_files = sorted([os.path.join(images_dir, file) for file in os.listdir(images_dir) if file.endswith('.png')])

# Load images
images = []
for image_file in image_files:
    img = Image.open(image_file)
    images.append(img)

# Save as GIF
imageio.mimsave(output_file, images, duration=0.1)  # duration is the time between frames in seconds

print(f"Rotating GIF saved as {output_file}")
