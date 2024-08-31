import os

# Change the working directory to src/data/NMR_Dataset/001
new_dir = os.path.join('src', 'data', 'NMR_Dataset', '001')
print(f"Changing working directory to: {new_dir}")
os.chdir(new_dir)
print(f"Current working directory: {os.getcwd()}")

# Function to remove .lst files in each subfolder
def remove_lst_files():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.lst'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed file: {file_path}")

# Remove existing .lst files
remove_lst_files()
print("Clean-up complete.")
