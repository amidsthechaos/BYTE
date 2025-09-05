# Substitution mapping
mapping = {
    "A": "B",
    "L": "Y",
    "O": "T",
    "K": "E"
}

# Your decoded Caesar/ROT13 result
cipher_text = "ALOK{alok_knvkfn_wgcyvgu_drkqfuu99}"

# Apply substitution mapping
decoded = ""
for ch in cipher_text:
    if ch.upper() in mapping:  # check if char is in mapping
        # preserve case
        if ch.isupper():
            decoded += mapping[ch.upper()]
        else:
            decoded += mapping[ch.upper()].lower()
    else:
        decoded += ch  # leave unchanged if not in mapping

print(decoded)

