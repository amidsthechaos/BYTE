def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

cipher = "NYBX{nybx_xaixsa_jtplith_qexdshh99}"

for s in range(26):
    print(f"Shift {s}: {caesar_shift(cipher, s)}")
