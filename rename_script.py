import os
from pathlib import Path
import shutil

# Define directories
source_dir = Path("data/dataset/SegmentationClassResize/")
destination_dir = Path("augmentation_data/masks/")

# Create the destination directory if it doesn't exist
destination_dir.mkdir(exist_ok=True)

# Get list of all image files in the source directory
image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')  # Add more if needed
image_files = [file for file in source_dir.iterdir() if file.suffix.lower() in image_extensions]

# Sort files to ensure consistent renaming
image_files.sort()

# Rename and save files in the 'rename' folder
for i, image_file in enumerate(image_files, start=1):
    if i > 100:
        break  # Stop if you want to rename only the first 100 images

    new_name = f"{i}{image_file.suffix}"  # New file name with the original extension
    new_path = destination_dir / new_name  # Destination path

    # Copy and rename the file
    shutil.copy(image_file, new_path)

    print(f"Renamed {image_file.name} to {new_name}")

print("Renaming complete!")
