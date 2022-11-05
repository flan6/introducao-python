def encode(frase: str):
    result = ""
    for char in frase:
        unicode = ord(char)
        letter = chr(unicode + 1)

        if unicode == 122:
            letter = chr(97)

        result = result + letter

    return result


def decode(frase):
    result_decodado = ""
    for char in frase:
        unicode = ord(char)
        letter = chr(unicode - 1)

        if unicode == 97:
            letter = chr(122)

        result_decodado = result_decodado + letter

    return result_decodado


entrada = input("digite para criptografar: ")

print(encode(entrada))
