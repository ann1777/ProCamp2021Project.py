import base64


def str_to_base64(msg):
    message_bytes = msg.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string
