import qrcode

img = qrcode.make("https://www.python.org")
img.save("python-org.png")
print("Saved python-org.png")
