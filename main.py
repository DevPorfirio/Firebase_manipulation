from Modules.Firebase import Firebase


firebase = Firebase(website='https://precatech-project-default-rtdb.firebaseio.com/')


if __name__ == '__main__':
    #firebase.get_pk_from_firebase(cpf=11111111111)
    #firebase.modify_user(cpf=11111111111, new_name="TESTE", new_cpf=10110110111, new_password="TESTE")
    firebase.create_user(name="TESTE", cpf=10010010011, password="TESTE")
    #firebase.delete_user(cpf=10010010011)
