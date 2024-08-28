'''
MIT License

Copyright (c) 2024 Jordi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
from PIL import Image
import pillow_heif

def convert_heic_to_png(input_folder):
    # Create the output folder if it doesn't exist
    output_folder = os.path.join(input_folder, 'png')
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.heic'):
            heic_file_path = os.path.join(input_folder, filename)
            png_file_name = os.path.splitext(filename)[0] + '.png'
            png_file_path = os.path.join(output_folder, png_file_name)

            try:
                # Open HEIC file using pillow_heif
                heif_file = pillow_heif.open_heif(heic_file_path)
                
                # Convert HEIC to PIL Image
                heif_image = heif_file[0]
                image_data = heif_image.data
                image = Image.frombytes(
                    heif_image.mode, 
                    heif_image.size, 
                    image_data, 
                    "raw", 
                    heif_image.mode, 
                    heif_image.stride
                )

                # Save as PNG
                image.save(png_file_path, "PNG")
                
                print(f"Converted {filename} to {png_file_name}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

def convert_single_heic_to_png(heic_file_path):
    '''
    Function I added to convert a single image and delete the original image.
    '''
    try:
        png_file_path = heic_file_path[:-5] + ".png" # cut off .heic
        
        # Open HEIC file using pillow_heif
        heif_file = pillow_heif.open_heif(heic_file_path)
        
        # Convert HEIC to PIL Image
        heif_image = heif_file[0]
        image_data = heif_image.data
        image = Image.frombytes(
            heif_image.mode, 
            heif_image.size, 
            image_data, 
            "raw", 
            heif_image.mode, 
            heif_image.stride
        )

        # Save as PNG
        image.save(png_file_path, "PNG")

        # Get rid of HEIC
        os.remove(heic_file_path) 
        
        print(f"Converted {heic_file_path} to {png_file_path}")
    except Exception as e:
        print(f"Failed to convert {heic_file_path}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing HEIC images: ")
    convert_heic_to_png(input_folder)