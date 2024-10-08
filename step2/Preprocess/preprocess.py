import cv2
import os
import xml.etree.ElementTree as ET

def process_images(image_folder, annotation_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(image_folder):
        print(f"Checking file: {filename}")  # Debugging
        if filename.endswith((".jpg", ".png")):  # Check for both formats
            image_path = os.path.join(image_folder, filename)
            annotation_path = os.path.join(annotation_folder, filename.replace(".png", ".xml").replace(".jpg", ".xml"))

            img = cv2.imread(image_path)
            if img is None:
                print(f"Image not found: {image_path}")
                continue  # Skip to the next image if not found

            print(f"Loaded image: {image_path}")

            if not os.path.exists(annotation_path):
                print(f"Annotation file not found: {annotation_path}")
                continue  # Skip if no annotation

            tree = ET.parse(annotation_path)
            root = tree.getroot()
            print(f"Processing annotations for: {filename}, found {len(root.findall('object'))} objects")

            for obj in root.findall('object'):
                bndbox = obj.find('bndbox')
                xmin = int(bndbox.find('xmin').text)
                ymin = int(bndbox.find('ymin').text)
                xmax = int(bndbox.find('xmax').text)
                ymax = int(bndbox.find('ymax').text)

                cropped_img = img[ymin:ymax, xmin:xmax]

                # Ensure that cropped_img is not empty
                if cropped_img.size == 0:
                    print(f"Empty cropped image for file: {filename}")
                    continue

                # Normalization (skip this step for display)
                # Gaussian Blur
                filtered_img = cv2.GaussianBlur(cropped_img, (5, 5), 0)

                # Convert to grayscale
                gray_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY)

                # Adjusted Thresholding
                _, segmented_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

                # Display segmented image
                cv2.imshow('Segmented Image', segmented_img)
                cv2.waitKey(0)

                # Save the segmented image
                output_path = os.path.join(output_folder, f"segmented_{filename}")
                cv2.imwrite(output_path, segmented_img)

    cv2.destroyAllWindows()

# Call the function with your folders
process_images(r'C:\Users\KIIT\OneDrive\Desktop\FlipkartGrid\DataSetPreparation\shubhamImages', 
               r'C:\Users\KIIT\OneDrive\Desktop\FlipkartGrid\DataSetPreparation\shubhamAnnonations', 
               'ShubhamProcessed')
