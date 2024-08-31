import os

categories = ['02958343', '04256520']  # Category IDs for cars and sofas
datadir = 'src/data/NMR_Dataset'
output_file = os.path.join(datadir, 'sofa_cars_gen.lst')

# Combine the gen_train.lst files from each category
with open(output_file, 'w') as outfile:
    for category in categories:
        train_list_path = os.path.join(datadir, category, 'gen_train.lst')
        with open(train_list_path, 'r') as infile:
            for line in infile:
                outfile.write(os.path.join(datadir, category, line))

print(f"Combined train list saved to {output_file}")
