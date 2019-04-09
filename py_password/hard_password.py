'''
Generate a ten-character alphanumeric password with at least one lowercase,
at least one uppercase character, and at least three digits
'''
import secrets
import string
alphabets = string.ascii_letters + string.digits
while True:
    password = "".join(secrets.choice(alphabets) for i in range(10))
    if(any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
            sum(c.isdigit() for c in password) >= 3):
        print(password)
        break
