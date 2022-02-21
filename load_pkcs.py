import rsa

privKey = rsa.PrivateKey.load_pkcs1(open("privKey.pem", "rb").read())

print(rsa.decrypt(open("1645217873.756811.bytes",
      "rb").read(), priv_key=privKey).decode())
