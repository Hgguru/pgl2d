import os

def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Split the filename and extension
            name, ext = os.path.splitext(filename)
            
            # Check if the filename is longer than 9 characters
            if len(name) > 9:
                if name[-9] == '_':
                    # Remove the last 9 characters from the name
                    new_name = name[:-9] + ext
                    
                    # Full path of the current file and new file
                    old_file = os.path.join(root, filename)
                    new_file = os.path.join(root, new_name)
                    
                    # Rename the file
                    os.rename(old_file, new_file)
                    print(f'Renamed: {old_file} -> {new_file}')
            else:
                print(f'Skipped (name too short): {os.path.join(root, filename)}')

if __name__ == '__main__':
    # Specify the directory you want to process
    directory = '.'
    rename_files_in_directory(directory)
