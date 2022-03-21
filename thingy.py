import glob
import time
import rsa

files = glob.glob("Bytes/*.bytes")
# print(files)
privKey = rsa.PrivateKey.load_pkcs1(open("privKey.pem", "rb").read())


def decryptRSA(files, key):
    arr = []
    for file in files:
        raw = open(file, "rb").read()
        data = rsa.decrypt(raw, key)
        arr.append(f'{data.decode()}\n')

    with open("output.tmp", "w+") as f:
        f.writelines(arr)
        f.close()
    return True


decryptRSA(files, privKey)
