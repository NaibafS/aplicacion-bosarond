import qrcode

# 👉 URL que querés codificar en el QR
url = "bosarond.mercadoshops.com.ar"

# Generar el objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Crear la imagen
img = qr.make_image(fill_color="black", back_color="white")

# Guardar en archivo
img.save("qr_web.png")

print("✅ QR generado en 'qr_web.png'")