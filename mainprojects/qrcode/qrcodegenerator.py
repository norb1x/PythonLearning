import sys
print(sys.path)
import qrcode
import image
qr = qrcode.QRCode(
  version = 15, 
  box_size = 20, 
  border = 5 
)

data = "https://www.youtube.com/watch?v=YgJmQC938ps"

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill="black",back_color = "white")
img.save("karamba")