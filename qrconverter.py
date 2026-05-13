from pyfiglet import figlet_format 
from PIL import Image
import qrcode
from urllib.parse import urlparse

opcion=""
print(figlet_format("Generador Qr", font="doom"))


url = input("Ingrese su url: ")
resultado=urlparse(url)
nombrearchivo=input("ingrese nombre del archivo a guardar: ")


if not resultado.scheme or not resultado.netloc :
    print("url invalidad")
else:
    print("generando qr ")
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make(fit=True)
    image=qr.make_image()
    
    ancho_qr, alto_qr=image.size
    
    image = image.convert("RGBA")
    
    opcion=input("quiere elegir agregar un logo a su qr? y/n: ")

    if opcion=="y":
        logo=input("Ingrese la ruta del logo a subir: ")

        logoqr=Image.open(logo)

        logoqr.save("logo.png")
        logoqr=Image.open("logo.png")
        logoqr=logoqr.convert("RGBA")
        ancho_logo, alto_logo =logoqr.size
        nuevologoAncho=int(ancho_qr*0.20)
        nuevologoAlto=int(alto_qr*0.20)
    
        logoqr=logoqr.resize((nuevologoAlto , nuevologoAncho))
    
        x = (ancho_qr - nuevologoAncho) / 2
        y = (alto_qr - nuevologoAlto) / 2
        image.paste(logoqr,(int(x),int(y)),mask=logoqr)
    else:
        print("generando qr")
image.save(nombrearchivo + ".png")