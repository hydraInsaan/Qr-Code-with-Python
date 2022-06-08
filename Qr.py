import pyqrcode
s = ("https://discord.gg/U5mUMpWuPW")
url = pyqrcode.create(s)
url.svg("PC Tricks's.svg", scale = 8)