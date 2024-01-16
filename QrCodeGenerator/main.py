import qrcode


def generate_qr_code(url:str):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data (in this case, the URL)
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="pink", back_color="blue")

    # Save the image
    imgName = url.replace("https://", "").split(".")[0] + ".png"
    img.save(imgName)
    print(f"Image saved: {imgName}")

if __name__ == "__main__":
    # Example usage
    website_url = "https://iv-portfolio.vercel.app/"

    generate_qr_code(website_url)
    # print(f"QR code generated and saved at {save_path}")
