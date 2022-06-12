import bcrypt

plain_text_password = "12345xyz"

hashed = bcrypt.hashpw(plain_text_password.encode('utf8'), bcrypt.gensalt(15))

print(hashed)

if bcrypt.checkpw(plain_text_password.encode('utf8'), hashed):
    print('correct password is entered')
else:
    print('password is incorrect. try again !')


##### with pepper
def add_pepper(pw):
    password_pepper = "tryhgvbnj$%&856#12lkQ!"
    return ".".join([pw, password_pepper])

plain_text_password = "12345xyz"
peppered_password = add_pepper(plain_text_password)

hashed = bcrypt.hashpw(peppered_password.encode('utf8'), bcrypt.gensalt(15))

print(hashed)

if bcrypt.checkpw(add_pepper(plain_text_password).encode('utf8'), hashed):
    print('correct password is entered')
else:
    print('password is incorrect. try again !')