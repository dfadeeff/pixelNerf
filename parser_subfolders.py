import os
import random

# Set random seed for reproducibility
random.seed(42)

# Path to the cars directory
cars_dir = 'src/data/NMR_Dataset/000'  # Update with your actual path

# Output file
output_file = 'src_gen_copy.txt'

# Function to parse directory and generate output
def parse_directory(base_dir, category_id, max_views=21):
    entries = []
    for subfolder in os.listdir(base_dir):
        subfolder_path = os.path.join(base_dir, subfolder)
        if os.path.isdir(subfolder_path):
            view_id = random.randint(0, max_views)
            entry = f"{category_id} {subfolder} {view_id}"
            entries.append(entry)
    return entries

# Main function
def main():
    category_id = '000'  # Car/chair category ID
    entries = parse_directory(cars_dir, category_id)
    with open(output_file, 'a') as f:
        for entry in entries:
            f.write(entry + '\n')
    print(f"Entries successfully written to {output_file}")

if __name__ == "__main__":
    main()
