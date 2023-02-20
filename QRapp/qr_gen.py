import qrcode
from qrcode.image.svg import SvgPathImage
import io


def generate(text):
    qr = qrcode.make(text, image_factory=SvgPathImage)
    return qr.to_string().decode('UTF-8')


def generate_png(text):
    qr = qrcode.make(text)
    buffer = io.BytesIO()
    qr.save(buffer, format='PNG')
    return buffer.getvalue()
