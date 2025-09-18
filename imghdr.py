# imghdr.py
# Reemplazo funcional mínimo para python-telegram-bot en Python 3.13
import os

def what(file, h=None):
    """
    Devuelve el tipo de imagen: 'jpeg', 'png', 'gif', 'bmp', etc.
    Solo soporta los formatos que usa python-telegram-bot.
    """
    if h is None:
        with open(file, 'rb') as f:
            h = f.read(32)
    if h[:3] == b'\xff\xd8\xff':
        return 'jpeg'
    if h[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    if h[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'
    if h[:2] == b'BM':
        return 'bmp'
    if h[:4] == b'RIFF' and h[8:12] == b'WEBP':
        return 'webp'
    return None
