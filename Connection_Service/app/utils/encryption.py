import ssl

def create_ssl_context(cafile, certfile, keyfile):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_verify_locations(cafile)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    return context
