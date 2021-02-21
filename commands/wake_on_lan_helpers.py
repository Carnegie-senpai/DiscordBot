from wakeonlan import send_magic_packet

async def send_wol():
    send_magic_packet("2C-F0-5D-72-4E-A9")
