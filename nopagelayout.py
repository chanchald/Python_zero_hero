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

    # Create a new blank A3 image
    a3_image = Image.new('RGB', a3_size, 'white')

    # Calculate the width and height of each image slot on the A3 page
    slot_width = a3_width // 2
    slot_height = a3_height // 4
    # List to hold the resized images
    resized_images = []

    current_row = 0
    current_col = 0

    current_page = 1  # Initialize current_page

    pdf_image_counter = 0  # Counter to track images on the current PDF page

    pdf = Image.new('RGB', (a3_width * 1, a3_height * 2), 'white')  # New PDF image

    for file in image_files:
        img_path = os.path.join(image_folder, file)
        # Open an image file
        img = Image.open(img_path)
        # Resize the image to fit into the slot
        img.thumbnail((slot_width, slot_height))
        # Paste the resized image onto the A3 image
        pdf.paste(img, (current_col * slot_width, current_row * slot_height))
        resized_images.append(img)

        pdf_image_counter += 1

        # Move to the next slot
        current_row += 1
        if current_row == 8:
            current_row = 0
            current_col += 1
            if current_col == 2 or pdf_image_counter == len(image_files):
                # Save the current A3 page as PDF
                pdf.save(output_pdf.format(current_page), save_all=True)
                print(f"PDF page {current_page} created successfully")
                # Create a new blank A3 image for the next page
                current_page += 1
                pdf = Image.new('RGB', (a3_width * 1, a3_height * 2), 'white')
                current_row = 0
                current_col = 0

    print("PDF created successfully.")

# Specify the folder containing images and the output PDF file
image_folder = r'C:\Users\admin\Documents\repos\aws-sa-associate-saac03\image_folder'
output_pdf = 'output{}.pdf'

# Start with page 1
current_page = 1

make_pdf(image_folder, output_pdf)
