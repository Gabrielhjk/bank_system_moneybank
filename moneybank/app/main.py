from database.crud import crud

name = input('Enter your name: ')
cpf = input('Enter your cpf: ')
password = input('Enter your password: ')
phone_number = input('Enter your phone_number: ')

if __name__ == "__main__":

    user = crud.create_user(
        name = name,
        cpf = cpf,
        password = password,
        transfer_password = 4537,
        phone_number = phone_number,
        balance = 100.43
    )
