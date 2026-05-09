import qrcode

url = input("Ingrese su url: ")

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)
qr.print_ascii(invert=True) 