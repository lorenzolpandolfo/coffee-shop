class User:
    def __init__(self, localid, nome, email, telefone):
        self.localid = localid
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def toDict(self):
        return {
            "nome": self.nome,
            "localid": self.localid,
            "email": self.email,
            "telefone": self.telefone
        }

