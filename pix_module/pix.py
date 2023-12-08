import qrcode
from PIL import Image
from pypix import Pix
import uuid


def criar_qr_code(preco:float):
    # Criar uma instância da classe Pix
    pix = Pix()

    id = str(int(uuid.uuid4()))[:15]

    # Definir os dados do Pix
    pix.set_pixkey("lorenzopandolfo2004@gmail.com")
    pix.set_description("Lo-Coffee shop")
    pix.set_merchant_name("Lo-Cafe")
    pix.set_merchant_city("Porto Alegre")
    pix.set_country_code("BR")
    pix.set_txid(id)
    pix.set_amount(preco)

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

    print(payload)

    # Salvar o QR Code como uma imagem
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("pix_qr_code.png")
    img.show()

criar_qr_code(10)