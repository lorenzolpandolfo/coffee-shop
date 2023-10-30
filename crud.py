import firebase_settings

auth = firebase_settings.auth
database = firebase_settings.database
storage = firebase_settings.storage
admin_auth = firebase_settings.admin_auth

# firebase_settings.auth.sign_in_with_email_and_password('lorenzopandolfo2004@gmail.com', 'senha123')

import add
import delete

if __name__ == '__main__':
    keep = True
    
    while keep:
        try:
            escolha = int(input("1. Apagar todas as contas\n2. Registrar um novo item\n3. Definir stand-by em um item existente\n" + 
                                "4. Excluir um item existente\n5. Listar itens registrados\n\n> Digite a opção desejada: "))

            # apagar todas as contas (apenas para testes de registro de usuario)
            if escolha == 1:
                userlist = admin_auth.list_users().iterate_all()
                for user in userlist:
                    admin_auth.delete_user(user.uid)
                    print("deletado!")
                    
            # registrar um novo item
            elif escolha == 2:
                item = add.criar_novo_item()
                if item:
                    print("[-] Item criado com sucesso. Enviando para o banco de dados...")
                    print(add.adicionar_novo_item(item))

            # Colocar item em stand-by (falta de estoque)
            elif escolha == 3:
                pass
            
            # Remover completamente um item
            elif escolha == 4: 
                delete.listar_todos_itens()
            
            else:
                keep = False
        
        except Exception as erro:
            print(f"[X] Erro: {erro}\n")
