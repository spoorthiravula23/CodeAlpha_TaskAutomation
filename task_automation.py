print("Welcome to CodeAlpha")
print("My First Python Automation Project")
import os
import shutil

# Source folder
source_folder = "MyFiles"

# Destination folder
destination_folder = "JPG_Images"

# Create destination folder
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

print("Destination folder created successfully!")
# Move image files
for file in os.listdir(source_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(file, "moved successfully!")