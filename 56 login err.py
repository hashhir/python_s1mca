user="hashh"
password="2727"
class validate(Exception):pass
try :
    u=input("enter username :")
    p=input("enter passcode :")
    if u==user and p==password:
        print("login successfull")
    else:
        raise validate('invalid login credential')
except validate as ve:
    print(ve)
