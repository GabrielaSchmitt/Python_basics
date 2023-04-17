# How to hash your passwords in python. Highly used in databases storage and validations. Here I`am using SHA256 encryption.
from hashlib import sha256
password = input("Password: ")

# encoding for storing
password = sha256(password.encode()).digest()

# when trying to Login, the service must compare the hashed password with the dashed input, as below:
login_password = input("Password: ")
hashed_login_password = sha256(login_password.encode()).digest()

print('Sucessfull Login') if hashed_login_password == password else print('Incorrect Password.')
