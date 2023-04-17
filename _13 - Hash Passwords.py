# How to hash your passwords in python. Highly used in databases storage and validations. Here I`m using SHA256 encryptation. 
from hashlib import sha256
password = input("Password: ")

# encoding for storaging
password = sha256(password.encode()).digest()

# when trying to Login, the service must compare the hashed password with the hashed imput, as bellow:
login_password = input("Password: ")
hashed_login_password = sha256(login_password.encode()).digest()

print('Sucessfull Login') if hashed_login_password == password else print('Incorrect Password.')
