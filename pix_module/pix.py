import qrcode
from PIL import Image
from pypix import Pix
import uuid

# Criar uma instância da classe Pix
pix = Pix()

# Definir os dados do Pix
pix.set_pixkey("lorenzopandolfo2004@gmail.com")
pix.set_description("Lo-Coffee shop")
pix.set_merchant_name("Lo-Cafe")
pix.set_merchant_city("Porto Alegre")
pix.set_country_code("BR")
pix.set_txid(str(uuid.uuid4))
pix.set_amount(3.1)

# Gerar o QR Code com Pix
payload = str(pix)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(payload)
qr.make(fit=True)

# Salvar o QR Code como uma imagem
img = qr.make_image(fill_color="black", back_color="white")
img.save("static/pix_qr_code.png")
img.show()
