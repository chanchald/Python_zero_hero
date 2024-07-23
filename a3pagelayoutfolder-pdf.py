from PIL import Image
import os

def make_pdf(image_folder, output_pdf):
    # Get all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

    # Sort the files if needed
    image_files.sort()

    # Define A3 size in pixels (11.7 x 16.5 inches at 300 DPI)
    a3_width = int(11.7 * 600)
    a3_height = int(16.5 * 600)
    a3_size = (a3_width, a3_height)

    # Calculate the width and height of each image slot on the A3 page
    slot_width = a3_width // 2
    slot_height = a3_height // 5

    current_page = 1  # Initialize current_page

    pdf = Image.new('RGB', (a3_width, a3_height), 'white')  # New PDF image

    for i, file in enumerate(image_files):
        img_path = os.path.join(image_folder, file)
        # Open an image file
        img = Image.open(img_path)
        # Resize the image to fit into the slot
        img.thumbnail((slot_width, slot_height))
        # Calculate the position of the image on the page
        pos_x = (i % 2) * slot_width
        pos_y = (i // 2 % 5) * slot_height
        # Paste the resized image onto the A3 image
        pdf.paste(img, (pos_x, pos_y))

        # If 8 images have been added or all images have been processed, save the page
        if (i + 1) % 10 == 0 or i + 1 == len(image_files):
            # Save the current A3 page as PDF
            pdf.save(output_pdf.format(current_page), "PDF")
            print(f"PDF page {current_page} created successfully")
            # Create a new blank A3 image for the next page
            current_page += 1
            pdf = Image.new('RGB', (a3_width, a3_height), 'white')

    print("PDF created successfully.")

# Specify the folder containing images and the output PDF file
image_folder = r'C:\Users\admin\Documents\repos\aws-sa-associate-saac03\2100-IAC_CLOUDFORMATION\image_folder'
output_pdf = 'output{}.pdf'

make_pdf(image_folder, output_pdf)
