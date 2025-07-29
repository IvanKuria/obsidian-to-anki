import os
from card_generator import generate_card_content

# ----------- Helper Functions -----------

def get_file_contents(path):
    with open(path, 'r') as f:
        return f.read()

def write_to_file(path, content, overwrite=False):
    mode = 'w' if overwrite else 'a'
    with open(path, mode) as f:
        f.write(content + '\n')

def process_file(file_path, output_path, overwrite=False):
    if file_path.endswith(".md"):
        print(f"Processing: {file_path}")
        content = generate_card_content(get_file_contents(file_path))
        write_to_file(output_path, content, overwrite)

def process_directory(folder_path, output_path, overwrite=False):
    first_write = overwrite
    for subdir, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                process_file(file_path, output_path, overwrite=first_write)
                first_write = False  # Only overwrite once