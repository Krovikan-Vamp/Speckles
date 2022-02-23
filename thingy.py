import glob
import rsa

files = glob.glob("Bytes/*.bytes")

privKey = rsa.PrivateKey.load_pkcs1(open("privKey.pem", "rb").read())


def decryptRSA(files, key):
    arr = []
    for file in files:
        data = rsa.decrypt(open(file, "rb").read(), key)
        arr.append(f'{data.decode()}\n')

    with open("output.txt", "w+") as f:
        f.writelines(arr)
        f.close()
    return True


decryptRSA(files, privKey)
