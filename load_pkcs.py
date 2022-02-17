import rsa

privKey = rsa.PrivateKey.load_pkcs1(open("privKey.pem", "rb").read())

print(rsa.decrypt(open("output.txt", "rb").read(), priv_key=privKey).center(
    len(open("output.txt", "rb").read())))
