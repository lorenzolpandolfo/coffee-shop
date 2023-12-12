from cryptography.fernet import Fernet


def gerar_chave():
    key = Fernet.generate_key()
    return key


def salvar_chave(key):
    with open("cryptkey.txt", "wb") as file:
        file.write(key)
    return "Nova chave criada com sucesso."


def get_key():
    with open("cryptkey.txt", "r") as file:
        return file.read()


def encrypt_dict(dc:dict):
    final_dc = {}
    fernet_key = get_key()
    fernet_object = Fernet(fernet_key)

    for chave, valor in dc.items():
        val = str(valor).encode()
        final_dc[chave] = str(fernet_object.encrypt(val))[1:].replace("'", "")

    return final_dc


def decrypt_dict(dc:dict, safe=True):
    final_dc = {}

    for chave, valor in dc.items():
        decrypted_value = Fernet(get_key()).decrypt(str(valor).encode()).decode("utf-8")
        
        if safe:
            if chave == "numero_cartao":
                final_dc[chave] = decrypted_value[12:]
            else:
                final_dc[chave] = decrypted_value

        else:
            final_dc[chave] = decrypted_value
    
    return final_dc


if __name__ == "__main__":
    print(salvar_chave(gerar_chave()))
