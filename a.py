from passlib.hash import bcrypt

password = bcrypt.hash("1234")
print(password)