from ..models.models import User, session

def create_user(name, cpf, password, transfer_password, phone_number, balance=0.0):
    new_user = User(name=name, cpf=cpf, password=password, transfer_password=transfer_password, phone_number=phone_number, balance=balance) 
    session.add(new_user)
    session.commit()
    return new_user
