import os
import cv2
from Priyadharsini import Priyadharsini
# Define the input and output folders
input_folder = 'DRIVE/test/mask'
output_folder = 'Preprocessed_images/test/mask'


# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all files in the input folder
input_files = os.listdir(input_folder)

# Loop through each file in the input folder
for filename in input_files:
    if filename.endswith(('.jpg', '.jpeg', '.png','.JPG','.tif')):  # You can add more file extensions as needed
        # Read the input image
        input_path = os.path.join(input_folder, filename)
        image = cv2.imread(input_path)

        if image is not None:
            # Apply your image processing algorithm here
            # For example, let's convert the image to grayscale
            processed_image = Priyadharsini(image)

            # Define the output file path
            output_path = os.path.join(output_folder, f"processed_{filename}")

            # Save the processed image
            cv2.imwrite(output_path, processed_image)
        else:
            print(f"Failed to read image: {input_path}")
    else:
        print(f"Unsupported file format: {filename}")

print("Image processing and saving complete.")
