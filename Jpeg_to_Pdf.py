from PIL import Image


def convert_jpeg_to_pdf(input_files, output_file):
    images = []
    for file in input_files:
        image = Image.open(file)
        images.append(image)

    images[0].save(output_file, "PDF", resolution=100.0,
                   save_all=True, append_images=images[1:])


# Example usage
input_files = ["001.jpg", "002.jpg"]
output_file = "output.pdf"
convert_jpeg_to_pdf(input_files, output_file)
