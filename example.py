## Using Bcrypt to Hash Passwords

# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# password = 'supersecretpassword'

# hashed_password = bcrypt.generate_password_hash(password, 10)

# print(hashed_password)

# check = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')
# print(check)


## Using Werkzeug to Hash passwords

from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('mypasswordishere')
print (hashed_pass)
check = check_password_hash(hashed_pass, 'mypasswordishere')
print(check)