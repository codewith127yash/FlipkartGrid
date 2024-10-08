import os
import shutil

# Paths based on your setup
mixed_folder = r"C:\Users\KIIT\OneDrive\Desktop\FlipkartGrid\shubham"  # Mixed folder path
image_folder = r"C:\Users\KIIT\OneDrive\Desktop\FlipkartGrid\DataSetPreparation\shubhamImages" # Images folder path
annotation_folder = r"C:\Users\KIIT\OneDrive\Desktop\FlipkartGrid\DataSetPreparation\shubhamAnnonations"  # Annotations folder path

# Create folders if they don't exist
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

if not os.path.exists(annotation_folder):
    os.makedirs(annotation_folder)

# Iterate through files in the mixed folder
for file in os.listdir(mixed_folder):
    file_path = os.path.join(mixed_folder, file)
    
    # Check if it's an image file (JPG or PNG)
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(file_path, image_folder)
    
    # Check if it's an annotation file (XML or JSON)
    elif file.endswith(".xml") or file.endswith(".json"):
        shutil.move(file_path, annotation_folder)

print("Files have been organized successfully!")
