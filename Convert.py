import cv2
import os
import imageio

# Specify the directory containing input files and the output directory for output files
input_directory = 'DRIVE/test/mask'
output_directory = 'DRIVE2/test/mask'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the input directory
input_files = [file for file in os.listdir(input_directory) if file.endswith(".gif")]

for input_file in input_files:
    input_path = os.path.join(input_directory, input_file)
    output_file = os.path.splitext(input_file)[0] + ".jpg"
    output_path = os.path.join(output_directory, output_file)

    try:
        # Read the input image using imageio
        gif = imageio.mimread(input_path)
        
        # Convert each frame to JPG and save it
        for i, frame in enumerate(gif):
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR (OpenCV uses BGR)
            jpg_output_path = output_path.replace(".jpg", f"_{i}.jpg")  # Append frame number to output path
            cv2.imwrite(jpg_output_path, frame)
            print(f"Conversion and save successful: {jpg_output_path}")

    except Exception as e:
        print(f"An error occurred while processing {input_file}: {e}")
