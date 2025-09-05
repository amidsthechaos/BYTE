import base64

encoded = "T1lCWHtueWJ4X3hhaXhzVV9qdHBsaXRoX3F1eGRzaG50X0"
encoded += "=" * (-len(encoded) % 4)   # auto-fix padding

decoded = base64.b64decode(encoded).decode("utf-8")
print(decoded)


import codecs

decoded = "NYBX{nybx_xaixsa_jtplith_qexdshh99}"
rot13 = codecs.decode(decoded, "rot_13")
print(rot13)