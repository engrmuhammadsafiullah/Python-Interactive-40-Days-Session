# Real-world third party packages handling complex pipelines (Run: pip install qrcode)
import qrcode

url_target = "https://python.org"
qr_image = qrcode.make(url_target)

# Export image object to hard drive file
qr_image.save("python_site.png")
print("Target QR matrix code exported safely to local file 'python_site.png'.")
