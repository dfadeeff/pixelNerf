import os
import glob
import imageio.v2 as imageio
import numpy as np

def is_blank_image(image):
    # Check if all pixels are the same
    return np.all(image == image[0,0])

def is_bad_image(image_path):
    try:
        img = imageio.imread(image_path)
        if img is None:
            print(f"Image is None: {image_path}")
            return True
        if img.size == 0:
            print(f"Image has zero size: {image_path}")
            return True
        if img.max() == 0:
            print(f"Image is completely black: {image_path}")
            return True
        if is_blank_image(img):
            print(f"Image is blank: {image_path}")
            return True
        return False
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
        return True

def clean_and_count_directory(base_path):
    valid_subfolders = []
    for root, dirs, files in os.walk(base_path):
        for dir_name in dirs:
            rgb_path = os.path.join(root, dir_name, "rgb")
            if not os.path.exists(rgb_path):
                continue

            has_valid_image = False
            for image_file in glob.glob(os.path.join(rgb_path, "*.png")):
                if not is_bad_image(image_file):
                    has_valid_image = True
                    break

            if has_valid_image:
                valid_subfolders.append(os.path.join(root, dir_name))
            else:
                subfolder_path = os.path.join(root, dir_name)
                print(f"Deleting subfolder: {subfolder_path}")
                os.system(f'rm -rf "{subfolder_path}"')

    return valid_subfolders

if __name__ == "__main__":
    base_path_val = "src/data/chairs_val"
    base_path_test = "src/data/chairs_test"

    valid_val_subfolders = clean_and_count_directory(base_path_val)
    valid_test_subfolders = clean_and_count_directory(base_path_test)

    print(f"Number of valid subfolders in validation set: {len(valid_val_subfolders)}")
    print(f"Number of valid subfolders in test set: {len(valid_test_subfolders)}")
