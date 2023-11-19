def xor_with_20(character):
    decimal_value = ord(character)
    xor_result = decimal_value ^ 32
    return xor_result

# Küçük "a" harfinden küçük "z" harfine kadar olan karakterler için işlemi gerçekleştir
print("Küçük harfler:")
for char_code in range(ord('a'), ord('z')+1):
    char = chr(char_code)
    result = xor_with_20(char)
    hex_result = hex(result)
    new_char = chr(result)
    print(f"{char}: {result} (Hex: {hex_result}) - Yeni Karakter: {new_char}")

# Büyük "A" harfinden büyük "Z" harfine kadar olan karakterler için işlemi gerçekleştir
print("\nBüyük harfler:")
for char_code in range(ord('A'), ord('Z')+1):
    char = chr(char_code)
    result = xor_with_20(char)
    hex_result = hex(result)
    new_char = chr(result)
    print(f"{char}: {result} (Hex: {hex_result}) - Yeni Karakter: {new_char}")
