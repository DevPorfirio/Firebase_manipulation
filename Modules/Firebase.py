import json
import requests


class Firebase(object):
    def __init__(self, website: str) -> None:
        self.website = website

    def create_user(self, name: str, cpf: int, password: str) -> json:
        """
        Criar usuário dentro do firebase
        :return: json
        """
        name_range = len(name)
        cpf_range = len(str(cpf))
        password_range = len(password)

        data = {'Nome': f'{name}', 'cpf': f'{cpf}', 'Senha': f'{password}'}
        if (name_range >= 1) and (cpf_range >= 1) and (password_range >= 1):
            if cpf_range == 11:
                try:
                    if self.get_pk_from_firebase(cpf) is None:
                        request = requests.post(f'{self.website}/Usuários/.json', data=json.dumps(data))
                        print(request)
                        return request
                    else:
                        print("Usuário já existe.")
                        return None
                except:
                    print('ERROR')
                    pass
            else:
                print('Digite apenas os 11 dígitos do CPF')
        else:
            print('Preencha todos os campos.')

    def modify_user(self, cpf: int, new_name: str = None, new_cpf: int = None, new_password: str = None):
        """
        Modificar usuário ja criado dentro do Firebase Realtime Database
        :return: json
        """
        pk = self.get_pk_from_firebase(cpf)
        cpf_range = len(str(new_cpf))
        name_range = len(new_name)
        password_range = len(new_password)

        if pk is None:
            print("Usuário não existe.")
            return None
        else:  # if the user exists
            if name_range > 1:
                data = {'Nome': f'{new_name}'}
                request = requests.patch(f'{self.website}/Usuários/{pk}/.json', data=json.dumps(data))
                print(request)

            if cpf_range == 11:
                data = {'cpf': f'{new_cpf}'}
                request = requests.patch(f'{self.website}/Usuários/{pk}/.json', data=json.dumps(data))
                print(request)

            if password_range >= 1:
                data = {'Senha': f'{new_password}'}
                request = requests.patch(f'{self.website}/Usuários/{pk}/.json', data=json.dumps(data))
                print(request)

            if name_range == 0 and cpf_range != 11 and password_range == 0:
                print('ERROR')
                return None

    def get_pk_from_firebase(self, cpf: int) -> str:
        """
        Obter a Primary Key do usuário a partir do seu grafo de CPF
        :param cpf: int
        :return: string
        """
        request = requests.get(f'{self.website}/Usuários/.json')
        dic_request = request.json()
        cpf_range = len(str(cpf))
        if cpf_range == 11:  # checks if the CPF was correctly inserted
            for pk in dic_request:
                scanned_cpf = dic_request[pk]['cpf']
                if scanned_cpf == f"{cpf}":
                    print(pk)
                    return pk
                else:
                    print('CPF não cadastrado.')
        else:
            print('Digite um CPF com 11 dígitos.')
        return None

    def delete_user(self, cpf: int) -> None:
        """
        Deletar o grafo de determinado usuário a partir do CPF
        :param cpf: int
        :return: None
        """
        cpf_range = len(str(cpf))
        if cpf_range == 11:
            pk = self.get_pk_from_firebase(cpf)
            request = requests.delete(f'{self.website}/Usuários/{pk}/.json')
            print(request)
        else:
            print('Digite um CPF com 11 dígitos.')
