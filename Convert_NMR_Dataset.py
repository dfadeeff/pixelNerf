import os
import numpy as np
from PIL import Image

# Define paths
nmr_data_dir = 'src/data/NMR_Dataset/02691156'  # Path to NMR dataset
output_dir = 'src/data/NMR_Dataset/converted_airplane'  # Path to save the converted dataset

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Function to convert a single subfolder
def convert_subfolder(subfolder_path, output_subfolder_path):
    cameras_path = os.path.join(subfolder_path, 'cameras.npz')
    if not os.path.exists(cameras_path):
        return 0

    cameras = np.load(cameras_path)

    # Extract keys for camera matrices and world matrices
    camera_keys = sorted([k for k in cameras.keys() if k.startswith('camera_mat_')])
    world_keys = sorted([k for k in cameras.keys() if k.startswith('world_mat_')])

    image_dir = os.path.join(subfolder_path, 'image')
    image_paths = sorted(os.listdir(image_dir))

    min_len = min(len(camera_keys), len(world_keys), len(image_paths))

    if len(camera_keys) != len(image_paths) or len(world_keys) != len(image_paths):
        print(f"Mismatch in number of camera/world matrices and images in {subfolder_path}. Using {min_len} elements.")

    # Create output directories for the subfolder
    os.makedirs(output_subfolder_path, exist_ok=True)
    os.makedirs(os.path.join(output_subfolder_path, 'pose'), exist_ok=True)
    os.makedirs(os.path.join(output_subfolder_path, 'rgb'), exist_ok=True)

    # Define intrinsics
    intrinsics_content = '131.250000 64.000000 64.000000 0.\n0. 0. 0.\n1.\n128 128\n'

    # Save intrinsics to a text file
    intrinsics_path = os.path.join(output_subfolder_path, 'intrinsics.txt')
    with open(intrinsics_path, 'w') as f:
        f.write(intrinsics_content)

    # Save images and poses
    for i in range(min_len):
        image_name = image_paths[i]
        image_path = os.path.join(image_dir, image_name)
        image = Image.open(image_path)
        image.save(os.path.join(output_subfolder_path, 'rgb', f'{i:06d}.png'))

        pose = cameras[world_keys[i]]
        pose_path = os.path.join(output_subfolder_path, 'pose', f'{i:06d}.txt')
        np.savetxt(pose_path, pose)

    return min_len

# Process each subfolder
for subfolder in sorted(os.listdir(nmr_data_dir)):
    subfolder_path = os.path.join(nmr_data_dir, subfolder)
    if os.path.isdir(subfolder_path):
        output_subfolder_path = os.path.join(output_dir, subfolder)
        convert_subfolder(subfolder_path, output_subfolder_path)

print(f'Converted dataset saved to {output_dir}')
