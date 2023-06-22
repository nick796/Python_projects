import qrcode

# Define your message
message = "https://www.youtube.com/results?search_query=gotcha"

# Create a QR code instance
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

# Add the message to the QR code
qr.add_data(message)
qr.make(fit=True)

# Create an image from the QR code
image = qr.make_image(fill_color="red", back_color="white")

# Save the image
image.save("qrcode.png")
