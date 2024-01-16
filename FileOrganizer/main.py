import os
import shutil


def organize_files(source_path):
    # Dictionary to map file extensions to their corresponding directories
    file_types = {
        'txt': 'TextFiles',
        'pdf': 'PDFs',
        'jpg': 'Images',
        'png': 'Images',
        'mp4': 'Videos',
        'mp3': 'Music',
        "pptx": "Presentations",
        "xlsx": "Excel Sheets"
    }
    created_directories = []
    # Create directories if they don't exist
    for directory in file_types.values():
        target_directory = os.path.join(source_path, directory)
        os.makedirs(target_directory, exist_ok=True)
        created_directories.append(target_directory)

    # Iterate through files in the source directory
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            # Remove the dot and convert to lowercase
            file_extension = file_extension.lower()[1:]

            # Determine the target directory for the file
            target_directory = file_types.get(file_extension, 'OtherFiles')
            target_directory = os.path.join(source_path, target_directory)

            # Move the file to the appropriate directory
            shutil.move(file_path, os.path.join(target_directory, filename))

     # Check if created folders are empty and delete them
    for directory in created_directories:
        if os.path.exists(directory) and not os.listdir(directory):
            os.rmdir(directory)
            print(f"Empty directory '{directory}' deleted.")
    print("File organization completed.")


# Example usage:
source_directory = '/mnt/Docs/My-Documents/Datastructures'
organize_files(source_directory)
