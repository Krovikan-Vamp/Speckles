const crypto = require('crypto');
const fs = require('fs')

const decryptedData = crypto.privateDecrypt({
    key: fs.readFileSync("./privKey.pem", { encoding: "utf-8" }),
    // padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
    oaepHash: "sha-256"
}, fs.readFileSync("./output.txt"))

console.log(decryptedData.toString())