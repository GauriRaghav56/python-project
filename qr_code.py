import qrcode

data = input("enter text or link:")
img = qrcode.make(data)
img.save("my qrcode.png")
img.show()
print("qr code ban gya !")