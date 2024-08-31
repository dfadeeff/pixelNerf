import os
import shutil
import random

# Define paths
dataset_dir = 'src/data/NMR_Dataset/converted_cars_sofa_bench_airplane'
output_dir = 'src/data/NMR_Dataset'
train_dir = os.path.join(output_dir, 'converted_cars_sofa_bench_airplane_train')
test_dir = os.path.join(output_dir, 'converted_cars_sofa_bench_airplane_test')
val_dir = os.path.join(output_dir, 'converted_cars_sofa_bench_airplane_val')

# Create output directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Get list of all subfolders
all_subfolders = [f for f in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, f))]

# Shuffle subfolders
random.shuffle(all_subfolders)

# Split into train, test, and val
train_split = int(0.7 * len(all_subfolders))
val_split = int(0.9 * len(all_subfolders))

train_subfolders = all_subfolders[:train_split]
val_subfolders = all_subfolders[train_split:val_split]
test_subfolders = all_subfolders[val_split:]

# Function to copy subfolders
def copy_subfolders(subfolder_list, src_folder, dest_folder):
    for subfolder in subfolder_list:
        src_path = os.path.join(src_folder, subfolder)
        dest_path = os.path.join(dest_folder, subfolder)
        try:
            shutil.copytree(src_path, dest_path)
        except OSError as e:
            print(f"Error: {e}")

# Copy subfolders to respective directories
copy_subfolders(train_subfolders, dataset_dir, train_dir)
copy_subfolders(val_subfolders, dataset_dir, val_dir)
copy_subfolders(test_subfolders, dataset_dir, test_dir)

print(f"Training subfolders: {len(train_subfolders)}")
print(f"Validation subfolders: {len(val_subfolders)}")
print(f"Testing subfolders: {len(test_subfolders)}")
